#!/usr/bin/env python3
"""
Comprehensive demo showing extensive dork generation with location parameters.
This demonstrates the complete production-ready functionality.
"""

from src.dork_generator import GrantDorkGenerator
import json
from datetime import datetime


def demo_extensive_dorks():
    """Demonstrate extensive dork generation for various use cases."""
    
    print("\n" + "=" * 80)
    print("EXTENSIVE GOOGLE DORK GENERATION - PRODUCTION DEMO")
    print("=" * 80)
    
    test_cases = [
        {
            "name": "Indigenous/Tribal Grants - Great Lakes Region",
            "topic": "indigenous tribal native american",
            "location": "Michigan, Minnesota, Wisconsin"
        },
        {
            "name": "Indigenous Education - Southwest",
            "topic": "indigenous education",
            "location": "Arizona, New Mexico"
        },
        {
            "name": "Healthcare - No Location",
            "topic": "healthcare technology",
            "location": None
        },
        {
            "name": "Single Location - California",
            "topic": "nonprofit capacity building",
            "location": "California"
        }
    ]
    
    results = []
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'─' * 80}")
        print(f"TEST CASE {i}: {test_case['name']}")
        print(f"{'─' * 80}")
        print(f"Topic: {test_case['topic']}")
        print(f"Location: {test_case['location'] or 'None'}")
        print()
        
        # Generate dorks
        dorks = GrantDorkGenerator.generate_all_dorks(
            topic=test_case['topic'],
            location=test_case['location']
        )
        
        # Display Google dork (most comprehensive)
        print("🔍 GOOGLE DORK:")
        print(f"{dorks['google'][:200]}...")  # First 200 chars
        print()
        
        # Verify key components
        google_dork = dorks['google']
        
        checks = {
            "Grant terms": "intext:grant" in google_dork and "inurl:funding" in google_dork,
            "Process wildcards": '"our grant ** process"' in google_dork,
            "Consideration": '"consideration"' in google_dork
        }
        
        # Add identity check for indigenous topics
        if "indigenous" in test_case['topic'] or "tribal" in test_case['topic']:
            checks["Identity terms"] = "intext:tribal" in google_dork or "intext:indigenous" in google_dork
            checks["Identity qualifications"] = '"tribal"' in google_dork and '"cib"' in google_dork
        
        # Add location check if provided
        if test_case['location']:
            locations = [loc.strip() for loc in test_case['location'].split(',')]
            checks["Location"] = all(f'"{loc}"' in google_dork for loc in locations)
        
        print("✅ VERIFICATION:")
        for check_name, passed in checks.items():
            status = "✓" if passed else "✗"
            print(f"  {status} {check_name}")
        
        all_passed = all(checks.values())
        
        results.append({
            "test_case": test_case['name'],
            "topic": test_case['topic'],
            "location": test_case['location'],
            "passed": all_passed,
            "checks": checks,
            "dorks": dorks
        })
        
        print()
        if all_passed:
            print("🎉 PASS")
        else:
            print("⚠️  FAIL - Some checks did not pass")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    total_tests = len(results)
    passed_tests = sum(1 for r in results if r['passed'])
    
    print(f"\nTotal Tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {total_tests - passed_tests}")
    print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
    
    print("\nDetailed Results:")
    for i, result in enumerate(results, 1):
        status = "✅ PASS" if result['passed'] else "❌ FAIL"
        print(f"  {i}. {result['test_case']}: {status}")
    
    # Save comprehensive example
    print("\n" + "=" * 80)
    print("SAVING EXAMPLE OUTPUT")
    print("=" * 80)
    
    example_output = {
        "generated_at": datetime.now().isoformat(),
        "description": "Extensive Google Dork Generation Examples",
        "test_results": [
            {
                "name": r['test_case'],
                "topic": r['topic'],
                "location": r['location'],
                "passed": r['passed'],
                "google_dork": r['dorks']['google'],
                "bing_dork": r['dorks']['bing'],
                "duckduckgo_dork": r['dorks']['duckduckgo']
            }
            for r in results
        ]
    }
    
    output_file = f"grant_dorks/extensive_demo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    try:
        with open(output_file, 'w') as f:
            json.dump(example_output, f, indent=2)
        print(f"✓ Saved to: {output_file}")
    except Exception as e:
        print(f"✗ Error saving: {e}")
    
    print("\n" + "=" * 80)
    
    return all(r['passed'] for r in results)


if __name__ == '__main__':
    success = demo_extensive_dorks()
    exit(0 if success else 1)
