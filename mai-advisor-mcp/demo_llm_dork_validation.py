"""
Demo: LLM-Guided Dork Generation with Schema Validation

This demonstrates how to use the dork_validator module to ensure
that LLMs generate properly formatted search dorks for each engine.
"""

from dork_generator import GrantDorkGenerator
from dork_validator import (
    SearchEngineType,
    DorkValidator,
    get_dork_generation_guidance
)


def demo_validation():
    """Demonstrate dork validation."""
    print("=" * 80)
    print("DORK VALIDATION DEMO")
    print("=" * 80)
    
    # Generate dorks
    topic = "indigenous tribal native american grants"
    location = "Michigan, Minnesota"
    
    dorks = GrantDorkGenerator.generate_all_dorks(topic, location)
    
    # Validate each dork
    for engine_name, dork in dorks.items():
        print(f"\n{engine_name.upper()} DORK:")
        print("-" * 80)
        print(dork)
        print()
        
        # Validate
        engine_type = SearchEngineType(engine_name)
        validator = DorkValidator(engine_type)
        result = validator.validate(dork)
        
        print(f"Valid: {'✓ YES' if result.is_valid else '✗ NO'}")
        
        if result.errors:
            print("\nErrors:")
            for error in result.errors:
                print(f"  - {error}")
        
        if result.warnings:
            print("\nWarnings:")
            for warning in result.warnings:
                print(f"  - {warning}")
        
        if result.suggestions:
            print("\nSuggestions:")
            for suggestion in result.suggestions:
                print(f"  - {suggestion}")
        
        print()


def demo_llm_guidance():
    """Demonstrate LLM guidance generation."""
    print("\n" + "=" * 80)
    print("LLM GUIDANCE DEMO")
    print("=" * 80)
    
    # Get guidance for Google
    print("\n### GOOGLE GUIDANCE SAMPLE ###\n")
    google_guidance = get_dork_generation_guidance('google')
    # Print first 1000 characters
    print(google_guidance[:1000])
    print("\n... (truncated) ...\n")
    
    # Get guidance for Bing
    print("\n### BING GUIDANCE SAMPLE ###\n")
    bing_guidance = get_dork_generation_guidance('bing')
    print(bing_guidance[:1000])
    print("\n... (truncated) ...\n")
    
    # Get guidance for DuckDuckGo
    print("\n### DUCKDUCKGO GUIDANCE SAMPLE ###\n")
    ddg_guidance = get_dork_generation_guidance('duckduckgo')
    print(ddg_guidance[:1000])
    print("\n... (truncated) ...\n")


def demo_validated_generation():
    """Demonstrate validated dork generation."""
    print("\n" + "=" * 80)
    print("VALIDATED GENERATION DEMO")
    print("=" * 80)
    
    topic = "community health grants for nonprofits"
    location = "California, Oregon"
    
    print(f"\nTopic: {topic}")
    print(f"Location: {location}\n")
    
    # Generate with validation
    results = GrantDorkGenerator.generate_validated_dorks(
        topic=topic,
        location=location,
        validate=True
    )
    
    # Display results
    for engine, data in results.items():
        print(f"\n{engine.upper()}:")
        print("-" * 80)
        print(f"Dork: {data['dork'][:200]}...")
        
        if 'validation' in data:
            validation = data['validation']
            print(f"Valid: {'✓' if validation.is_valid else '✗'}")
            
            if validation.errors:
                print("Errors:", validation.errors)
            if validation.warnings:
                print("Warnings:", validation.warnings)
        
        print()


def demo_llm_integration_example():
    """
    Example of how to integrate schema validation into an LLM prompt.
    
    This shows how you would structure a prompt to an LLM to ensure
    it generates properly formatted dorks.
    """
    print("\n" + "=" * 80)
    print("LLM INTEGRATION EXAMPLE")
    print("=" * 80)
    
    # Get the guidance
    google_guidance = get_dork_generation_guidance('google')
    
    # Example user request
    user_request = "Find grants for STEM education in underserved communities"
    
    # Construct LLM prompt
    llm_prompt = f"""
You are a search expert. Generate a Google search dork for the following request:

USER REQUEST: {user_request}

{google_guidance}

Generate a properly formatted Google dork that follows all the rules above.
Include:
1. Core grant terminology with intext/inurl variations
2. Topic-specific terms (STEM, education, underserved)
3. Process indicators
4. Appropriate site: and filetype: operators

Output only the dork query, no explanation.
"""
    
    print("\nLLM PROMPT TEMPLATE:")
    print("-" * 80)
    print(llm_prompt)
    print()
    
    print("\nEXPECTED LLM OUTPUT FORMAT:")
    print("-" * 80)
    print('(intext:grant OR inurl:grant OR intext:funding OR inurl:funding OR intext:application OR inurl:application) ("STEM" OR "science education" OR "technology education") ("underserved" OR "underrepresented" OR "low income") ("application process" OR "eligibility" OR "how to apply") (site:ed.gov OR site:nsf.gov OR site:grants.gov) filetype:pdf')
    print()


def save_guidance_to_file():
    """Save all guidance to a file for LLM system prompts."""
    print("\n" + "=" * 80)
    print("SAVING GUIDANCE TO FILE")
    print("=" * 80)
    
    guidance_all = GrantDorkGenerator.get_llm_guidance("all")
    
    output_file = "llm_dork_generation_guidance.txt"
    
    with open(output_file, 'w') as f:
        f.write("=" * 80 + "\n")
        f.write("COMPREHENSIVE DORK GENERATION GUIDANCE FOR LLMs\n")
        f.write("=" * 80 + "\n\n")
        
        for engine, guidance in guidance_all.items():
            f.write(f"\n{'=' * 80}\n")
            f.write(f"{engine.upper()} GUIDANCE\n")
            f.write(f"{'=' * 80}\n\n")
            f.write(guidance)
            f.write("\n\n")
    
    print(f"\n✓ Guidance saved to: {output_file}")
    print("  This file can be included in LLM system prompts to ensure proper dork generation.\n")


if __name__ == '__main__':
    # Run all demos
    demo_validation()
    demo_llm_guidance()
    demo_validated_generation()
    demo_llm_integration_example()
    save_guidance_to_file()
    
    print("\n" + "=" * 80)
    print("DEMO COMPLETE")
    print("=" * 80)
    print("\nKey Takeaways:")
    print("1. Use get_dork_generation_guidance() to get LLM prompts")
    print("2. Include guidance in system prompts for proper dork generation")
    print("3. Validate generated dorks with DorkValidator")
    print("4. Different rules apply to each search engine")
    print("5. DuckDuckGo requires multiple simple queries instead of complex dorks")
    print()
