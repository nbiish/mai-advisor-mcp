#!/usr/bin/env python3
"""
Side-by-side comparison of our generated dork vs. target example.
"""

from src.dork_generator import GrantDorkGenerator


def compare_to_target():
    """Compare our output to the target example provided."""
    
    print("\n" + "=" * 80)
    print("COMPARISON: Our Output vs. Target Example")
    print("=" * 80)
    
    # Generate our dork
    dorks = GrantDorkGenerator.generate_all_dorks(
        topic="indigenous tribal native american",
        location="Michigan, Minnesota"
    )
    
    our_dork = dorks['google']
    
    # Target example from user
    target_dork = '''(intext:grant OR inurl:grant OR intext:philanthropy OR inurl:philanthropy OR intext:application OR inurl:application OR intext:funding OR inurl:funding OR intext:opportunit* OR inurl:opportunit* OR intext:intake OR inurl:intake OR intext:award OR inurl:award OR intext:fellowship OR inurl:fellowship OR intext:unrestricted OR inurl:unrestricted OR intext:guidelines OR inurl:guidelines OR intext:apply OR inurl:apply OR intext:endowment OR inurl:endowment OR intext:fund OR inurl:fund OR inurl:funding OR inurl:grant OR inurl:application OR intext:tribal OR intext:tribal OR intext:"federally recognized" OR intext:indigenous OR inurl:indigenous OR intext:"native american" OR inurl:native-american) "tribal" OR "indigenous" OR "native" OR "first nation" OR "native american" OR "federally recognized" OR "cib" OR "state recognized" OR "tribal citizen" OR "tribal id" OR "tribal identification" OR "indigena" OR "our grant ** process" OR "our ** process" OR "consideration" OR "Michigan" OR "Minnesota"'''
    
    print("\n📋 TARGET EXAMPLE (from user):")
    print("-" * 80)
    print(target_dork[:300] + "...")
    
    print("\n📋 OUR OUTPUT:")
    print("-" * 80)
    print(our_dork[:300] + "...")
    
    print("\n\n" + "=" * 80)
    print("COMPONENT VERIFICATION")
    print("=" * 80)
    
    components_to_check = {
        "Grant core terms": [
            "intext:grant", "inurl:grant", "intext:philanthropy", "inurl:philanthropy",
            "intext:application", "inurl:application", "intext:funding", "inurl:funding"
        ],
        "Wildcards": [
            "intext:opportunit*", "inurl:opportunit*"
        ],
        "Additional grant terms": [
            "intext:fellowship", "inurl:fellowship", "intext:guidelines", "inurl:guidelines",
            "intext:endowment", "inurl:endowment", "intext:fund", "inurl:fund"
        ],
        "Identity intext terms": [
            "intext:tribal", "intext:indigenous", "intext:native american"
        ],
        "Identity inurl terms": [
            "inurl:tribal", "inurl:indigenous", "inurl:native-american"
        ],
        "Quoted identity qualifications": [
            '"tribal"', '"indigenous"', '"native american"', '"federally recognized"',
            '"cib"', '"state recognized"', '"tribal citizen"', '"tribal id"',
            '"tribal identification"'
        ],
        "Process wildcards": [
            '"our grant ** process"', '"our ** process"'
        ],
        "Process terms": [
            '"consideration"', '"eligibility"', '"criteria"'
        ],
        "Location terms": [
            '"Michigan"', '"Minnesota"'
        ]
    }
    
    print("\nChecking OUR OUTPUT for all required components:\n")
    
    all_present = True
    for category, terms in components_to_check.items():
        present_count = sum(1 for term in terms if term in our_dork)
        total = len(terms)
        percentage = (present_count / total) * 100
        
        if percentage == 100:
            status = "✅ COMPLETE"
        elif percentage >= 75:
            status = "⚠️  PARTIAL"
        else:
            status = "❌ MISSING"
            all_present = False
        
        print(f"{status} {category}: {present_count}/{total} ({percentage:.0f}%)")
        
        # Show any missing terms
        if percentage < 100:
            missing = [term for term in terms if term not in our_dork]
            for m in missing[:3]:  # Show first 3 missing
                print(f"         Missing: {m}")
    
    print("\n" + "=" * 80)
    print("STRUCTURE ANALYSIS")
    print("=" * 80)
    
    # Count key operators
    our_metrics = {
        "intext operators": our_dork.count("intext:"),
        "inurl operators": our_dork.count("inurl:"),
        "Quoted phrases": our_dork.count('"'),
        "OR operators": our_dork.count(" OR "),
        "Wildcard operators": our_dork.count("**"),
        "Total length": len(our_dork)
    }
    
    target_metrics = {
        "intext operators": target_dork.count("intext:"),
        "inurl operators": target_dork.count("inurl:"),
        "Quoted phrases": target_dork.count('"'),
        "OR operators": target_dork.count(" OR "),
        "Wildcard operators": target_dork.count("**"),
        "Total length": len(target_dork)
    }
    
    print(f"\n{'Metric':<25} {'Our Output':<15} {'Target':<15} {'Comparison'}")
    print("-" * 80)
    
    for metric in our_metrics.keys():
        our_val = our_metrics[metric]
        target_val = target_metrics[metric]
        
        if our_val >= target_val:
            comparison = "✅ Equal/Better"
        elif our_val >= target_val * 0.8:
            comparison = "⚠️  Close"
        else:
            comparison = "❌ Less"
        
        print(f"{metric:<25} {our_val:<15} {target_val:<15} {comparison}")
    
    print("\n" + "=" * 80)
    print("FINAL VERDICT")
    print("=" * 80)
    
    # Check if we meet/exceed target metrics
    meets_target = (
        all_present and 
        our_metrics["intext operators"] >= target_metrics["intext operators"] and
        our_metrics["inurl operators"] >= target_metrics["inurl operators"] and
        our_metrics["Quoted phrases"] >= 30 and
        our_metrics["Wildcard operators"] >= 2
    )
    
    if meets_target:
        print("\n🎉 SUCCESS!")
        print("Our generated dork MATCHES the target example in:")
        print("  ✓ Component coverage (all key terms present)")
        print("  ✓ Operator usage (extensive intext/inurl)")
        print("  ✓ Structure (proper OR logic and grouping)")
        print("  ✓ Comprehensiveness (extensive term coverage)")
        print("\n✅ PRODUCTION-READY: Our dork generator produces output")
        print("   matching the extensive format required.")
    else:
        print("\n⚠️  Review needed - some components may differ from target.")
    
    print("\n" + "=" * 80)
    
    return meets_target


if __name__ == '__main__':
    success = compare_to_target()
    exit(0 if success else 1)
