"""
Production-grade Google Dork Generator for Grant Finding
Generates extensive, comprehensive search queries with intext/inurl variations

Integrates with dork_validator.py to ensure search engine schema compliance.
"""
from typing import List, Dict, Optional, Union
from dataclasses import dataclass

# Import validation components (optional - only used if validation is requested)
try:
    from dork_validator import (
        SearchEngineType,
        DorkValidator,
        get_dork_generation_guidance
    )
    VALIDATOR_AVAILABLE = True
except ImportError:
    VALIDATOR_AVAILABLE = False


@dataclass
class DorkInput:
    """Simplified input for dork generation."""
    topic: str  # Main topic/focus (e.g., "indigenous education")
    location: Optional[str] = None  # Geographic focus (e.g., "Michigan, Minnesota")


class GrantDorkGenerator:
    """
    Generate production-quality Google dorks for grant finding.
    Based on proven patterns from actual non-profit grant searches.
    """
    
    # Comprehensive grant-related terminology with intext/inurl variants
    GRANT_CORE_TERMS = [
        'grant', 'philanthropy', 'application', 'funding', 
        'opportunit*', 'intake', 'award', 'fellowship',
        'unrestricted', 'guidelines', 'apply', 'endowment', 'fund'
    ]
    
    # Topic-specific identity terms and variants (expanded dynamically based on topic)
    TOPIC_IDENTITY_MAPS = {
        'indigenous': [
            'tribal', 'indigenous', 'native american', 'first nation',
            'native', 'federally recognized'
        ],
        'tribal': [
            'tribal', 'indigenous', 'native american', 'first nation',
            'native', 'federally recognized'
        ],
        'native': [
            'tribal', 'indigenous', 'native american', 'first nation',
            'native', 'federally recognized'
        ],
        'native american': [
            'tribal', 'indigenous', 'native american', 'first nation',
            'native', 'federally recognized'
        ]
    }
    
    # Grant process indicators
    GRANT_PROCESS_TERMS = [
        '"our grant ** process"',
        '"our ** process"',
        '"application process"',
        '"how to apply"',
        '"submit application"',
        '"request for proposals"',
        '"rfp"',
        '"letter of inquiry"',
        '"loi"',
        '"eligibility"',
        '"criteria"',
        '"consideration"'
    ]
    
    # Identity-specific qualification terms (for tribal/indigenous searches)
    IDENTITY_QUALIFICATION_TERMS = {
        'indigenous': [
            'tribal', 'indigenous', 'native', 'first nation', 'native american',
            'federally recognized', 'cib', 'state recognized', 'tribal citizen',
            'tribal id', 'tribal identification', 'indigena'
        ],
        'tribal': [
            'tribal', 'indigenous', 'native', 'first nation', 'native american',
            'federally recognized', 'cib', 'state recognized', 'tribal citizen',
            'tribal id', 'tribal identification', 'indigena'
        ],
        'native': [
            'tribal', 'indigenous', 'native', 'first nation', 'native american',
            'federally recognized', 'cib', 'state recognized', 'tribal citizen',
            'tribal id', 'tribal identification', 'indigena'
        ],
        'native american': [
            'tribal', 'indigenous', 'native', 'first nation', 'native american',
            'federally recognized', 'cib', 'state recognized', 'tribal citizen',
            'tribal id', 'tribal identification', 'indigena'
        ]
    }
    
    # File types commonly containing grant info
    GRANT_FILETYPES = ['pdf', 'doc', 'docx']
    
    # Trusted grant sites (government, foundations, databases)
    TRUSTED_SITES = [
        'grants.gov', 'nsf.gov', 'nih.gov', 'ed.gov', 'neh.gov', 'nea.gov',
        'candid.org', 'foundationcenter.org', 'foundationsource.com',
        'grantwatch.com', 'grantsolutions.gov', 'foundationlist.org'
    ]
    
    @staticmethod
    def extract_keywords_from_topic(topic: str) -> List[str]:
        """
        Extract searchable keywords from natural language topic.
        Handles phrases like 'indigenous education technology'.
        """
        # Remove common stop words but keep meaningful phrases
        stop_words = {'for', 'the', 'and', 'or', 'in', 'on', 'at', 'to', 'a', 'an'}
        
        words = topic.lower().split()
        keywords = [w.strip() for w in words if w.strip() not in stop_words]
        
        # Also keep the full phrase
        if len(keywords) > 1:
            keywords.insert(0, topic.lower())
        
        return keywords
    
    @classmethod
    def _detect_identity_context(cls, topic: str) -> Optional[str]:
        """
        Detect if topic relates to specific identity (indigenous, tribal, etc.)
        Returns the identity key if detected, None otherwise.
        """
        topic_lower = topic.lower()
        for identity_key in cls.TOPIC_IDENTITY_MAPS.keys():
            if identity_key in topic_lower:
                return identity_key
        return None
    
    @classmethod
    def _build_intext_inurl_clause(cls, terms: List[str], include_url_variations: bool = True) -> str:
        """
        Build comprehensive intext/inurl OR clause for terms.
        Example: (intext:grant OR inurl:grant OR intext:funding OR inurl:funding ...)
        
        Args:
            terms: List of terms to include
            include_url_variations: If True, adds both intext: and inurl: for each term
        """
        clauses = []
        for term in terms:
            clauses.append(f'intext:{term}')
            if include_url_variations:
                clauses.append(f'inurl:{term}')
        return f"({' OR '.join(clauses)})"
    
    @classmethod
    def _build_keyword_variants(cls, keywords: List[str]) -> str:
        """
        Build quoted keyword variants with OR logic.
        Handles both single words and multi-word phrases.
        """
        variants = []
        for kw in keywords:
            variants.append(f'"{kw}"')
            # Add variant with wildcards for flexibility
            if ' ' in kw:
                # Multi-word: add each word individually too
                for word in kw.split():
                    if len(word) > 3:  # Skip short words
                        variants.append(f'"{word}"')
        
        return ' OR '.join(variants)
    
    @classmethod
    def _build_location_clause(cls, location: Optional[str]) -> str:
        """
        Build location targeting clause.
        Handles comma-separated locations (e.g., "Michigan, Minnesota")
        """
        if not location:
            return ''
        
        locations = [loc.strip() for loc in location.split(',')]
        location_terms = [f'"{loc}"' for loc in locations if loc]
        
        return ' OR '.join(location_terms)
    
    @classmethod
    def generate_google_dork(cls, input_data: DorkInput) -> str:
        """
        Generate comprehensive Google dork query matching extensive production format.
        
        Structure:
        1. Core grant terms with intext/inurl variants
        2. Identity-specific terms with intext/inurl (if applicable)
        3. Identity qualification terms (quoted phrases)
        4. Grant process indicators with wildcards
        5. Location targeting
        
        Example output format:
        (intext:grant OR inurl:grant OR ... OR inurl:fund) 
        (intext:tribal OR intext:indigenous OR ...)
        "tribal" OR "indigenous" OR ... OR "tribal identification"
        "our grant ** process" OR "consideration" OR ...
        "Michigan" OR "Minnesota"
        """
        keywords = cls.extract_keywords_from_topic(input_data.topic)
        identity_context = cls._detect_identity_context(input_data.topic)
        
        parts = []
        
        # Part 1: Comprehensive grant terminology with intext/inurl
        grant_clause = cls._build_intext_inurl_clause(cls.GRANT_CORE_TERMS)
        
        # Part 2: Add identity-specific intext/inurl if detected
        if identity_context and identity_context in cls.TOPIC_IDENTITY_MAPS:
            identity_terms = cls.TOPIC_IDENTITY_MAPS[identity_context]
            # Add intext variations for identity terms
            identity_intext_clauses = [f'intext:{term}' for term in identity_terms]
            # Also add inurl variations
            identity_inurl_clauses = [f'inurl:{term.replace(" ", "-")}' for term in identity_terms]
            combined_grant_identity = grant_clause[:-1] + ' OR ' + ' OR '.join(identity_intext_clauses + identity_inurl_clauses) + ')'
            parts.append(combined_grant_identity)
        else:
            parts.append(grant_clause)
        
        # Part 3: Identity qualification terms as quoted phrases (if applicable)
        if identity_context and identity_context in cls.IDENTITY_QUALIFICATION_TERMS:
            qualification_terms = cls.IDENTITY_QUALIFICATION_TERMS[identity_context]
            quoted_qualifications = [f'"{term}"' for term in qualification_terms]
            parts.append(' OR '.join(quoted_qualifications))
        else:
            # For non-identity topics, add topic keywords as quoted phrases
            keyword_clause = cls._build_keyword_variants(keywords)
            parts.append(keyword_clause)
        
        # Part 4: Grant process indicators (always included)
        process_clause = ' OR '.join(cls.GRANT_PROCESS_TERMS)
        parts.append(process_clause)
        
        # Part 5: Location targeting (if provided)
        if input_data.location:
            location_clause = cls._build_location_clause(input_data.location)
            parts.append(location_clause)
        
        # Combine all parts with spaces
        dork = ' '.join(parts)
        
        return dork
    
    @classmethod
    def generate_bing_dork(cls, input_data: DorkInput) -> str:
        """
        Generate Bing-optimized dork.
        Bing supports: intitle, inbody, inanchor, loc, site, filetype
        """
        keywords = cls.extract_keywords_from_topic(input_data.topic)
        
        parts = []
        
        # Use inbody for grant terms (Bing equivalent of intext)
        grant_terms_quoted = ' OR '.join([f'"{term}"' for term in cls.GRANT_CORE_TERMS[:10]])
        parts.append(f'({grant_terms_quoted})')
        
        # Keywords with intitle for better relevance
        if keywords:
            main_kw = keywords[0]
            parts.append(f'intitle:"{main_kw}"')
            if len(keywords) > 1:
                other_kws = ' OR '.join([f'"{kw}"' for kw in keywords[1:]])
                parts.append(f'({other_kws})')
        
        # Location with loc: operator
        if input_data.location:
            locations = [loc.strip() for loc in input_data.location.split(',')]
            if locations:
                parts.append(f'loc:"{locations[0]}"')
        
        # Add grant process terms
        parts.append('("application" OR "apply" OR "deadline" OR "eligibility")')
        
        return ' '.join(parts)
    
    @classmethod
    def generate_duckduckgo_dork(cls, input_data: DorkInput) -> str:
        """
        Generate DuckDuckGo-optimized dork.
        DDG supports: site, intitle, inurl, filetype, but limited complex queries
        Keep simpler for DDG compatibility.
        """
        keywords = cls.extract_keywords_from_topic(input_data.topic)
        
        parts = []
        
        # Main keywords
        if keywords:
            main_kw = keywords[0]
            parts.append(f'"{main_kw}"')
        
        # Core grant terms (simplified for DDG)
        parts.append('(grant OR funding OR fellowship OR application)')
        
        # Location
        if input_data.location:
            locations = [loc.strip() for loc in input_data.location.split(',')]
            location_quoted = ' OR '.join([f'"{loc}"' for loc in locations])
            parts.append(f'({location_quoted})')
        
        # Add intitle for grant-specific pages
        parts.append('(intitle:grant OR intitle:funding OR intitle:apply)')
        
        # Process terms
        parts.append('("deadline" OR "eligibility" OR "guidelines")')
        
        return ' '.join(parts)
    
    @classmethod
    def generate_all_dorks(cls, topic: str, location: Optional[str] = None) -> Dict[str, str]:
        """
        Generate dorks for all three search engines.
        
        Returns:
            Dict with keys 'google', 'bing', 'duckduckgo' containing dork strings
        """
        input_data = DorkInput(topic=topic, location=location)
        
        return {
            'google': cls.generate_google_dork(input_data),
            'bing': cls.generate_bing_dork(input_data),
            'duckduckgo': cls.generate_duckduckgo_dork(input_data)
        }
    
    @classmethod
    def generate_validated_dorks(
        cls, 
        topic: str, 
        location: Optional[str] = None,
        validate: bool = True
    ) -> Dict[str, Dict]:
        """
        Generate dorks with validation and schema guidance.
        
        Args:
            topic: Search topic
            location: Geographic location(s)
            validate: Whether to validate generated dorks
        
        Returns:
            Dict with keys for each search engine containing:
                - dork: The generated dork string (or list for DDG)
                - validation: Validation results if validate=True
                - guidance: LLM generation guidance for this engine
                - examples: Verified examples for this engine
        """
        if validate and not VALIDATOR_AVAILABLE:
            raise ImportError("dork_validator module not available. Install dependencies.")
        
        input_data = DorkInput(topic=topic, location=location)
        results = {}
        
        # Google
        google_dork = cls.generate_google_dork(input_data)
        results['google'] = {
            'dork': google_dork,
            'engine': 'google'
        }
        
        if validate:
            validator = DorkValidator(SearchEngineType.GOOGLE)
            results['google']['validation'] = validator.validate(google_dork)
        
        # Bing
        bing_dork = cls.generate_bing_dork(input_data)
        results['bing'] = {
            'dork': bing_dork,
            'engine': 'bing'
        }
        
        if validate:
            validator = DorkValidator(SearchEngineType.BING)
            results['bing']['validation'] = validator.validate(bing_dork)
        
        # DuckDuckGo
        ddg_dork = cls.generate_duckduckgo_dork(input_data)
        results['duckduckgo'] = {
            'dork': ddg_dork,
            'engine': 'duckduckgo'
        }
        
        if validate:
            validator = DorkValidator(SearchEngineType.DUCKDUCKGO)
            results['duckduckgo']['validation'] = validator.validate(ddg_dork)
        
        return results
    
    @classmethod
    def get_llm_guidance(cls, engine: str = "all") -> Union[str, Dict[str, str]]:
        """
        Get LLM generation guidance for dork creation.
        
        This provides the comprehensive schema documentation and examples
        that an LLM should follow when generating dorks.
        
        Args:
            engine: 'google', 'bing', 'duckduckgo', or 'all'
        
        Returns:
            Guidance string or dict of guidance strings for all engines
        """
        if not VALIDATOR_AVAILABLE:
            raise ImportError("dork_validator module not available. Install dependencies.")
        
        if engine == "all":
            return {
                'google': get_dork_generation_guidance('google'),
                'bing': get_dork_generation_guidance('bing'),
                'duckduckgo': get_dork_generation_guidance('duckduckgo')
            }
        else:
            return get_dork_generation_guidance(engine)


# Example usage for testing
if __name__ == '__main__':
    # Test with tribal/indigenous example
    dorks = GrantDorkGenerator.generate_all_dorks(
        topic="indigenous tribal native american grants",
        location="Michigan, Minnesota"
    )
    
    print("=" * 80)
    print("GOOGLE DORK:")
    print("=" * 80)
    print(dorks['google'])
    print("\n" + "=" * 80)
    print("BING DORK:")
    print("=" * 80)
    print(dorks['bing'])
    print("\n" + "=" * 80)
    print("DUCKDUCKGO DORK:")
    print("=" * 80)
    print(dorks['duckduckgo'])
