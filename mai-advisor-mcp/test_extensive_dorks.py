#!/usr/bin/env python3
"""Test that dork generator produces extensive queries matching production examples."""

from src.dork_generator import GrantDorkGenerator

def test_indigenous_extensive_dork():
    """Test indigenous/tribal dork generation matches extensive format."""
    
    print("=" * 80)
    print("Testing Extensive Dork Generation for Indigenous/Tribal Grants")
    print("=" * 80)
    
    # Generate dorks
    dorks = GrantDorkGenerator.generate_all_dorks(
        topic="indigenous tribal native american grants",
        location="Michigan, Minnesota"
    )
    
    google_dork = dorks['google']
    
    print("\n📋 GOOGLE DORK OUTPUT:")
    print("-" * 80)
    print(google_dork)
    print("-" * 80)
    
    # Verify key components are present
    print("\n✅ VERIFICATION CHECKS:")
    print("-" * 80)
    
    checks = {
        "Grant terms with intext/inurl": [
            "intext:grant", "inurl:grant", "intext:funding", "inurl:funding",
            "intext:fellowship", "inurl:fellowship"
        ],
        "Identity terms with intext": [
            "intext:tribal", "intext:indigenous", "intext:native american"
        ],
        "Identity terms with inurl": [
            "inurl:tribal", "inurl:indigenous", "inurl:native-american"
        ],
        "Quoted identity qualifications": [
            '"tribal"', '"indigenous"', '"native american"', '"federally recognized"',
            '"cib"', '"state recognized"', '"tribal citizen"', '"tribal id"'
        ],
        "Process terms with wildcards": [
            '"our grant ** process"', '"our ** process"', '"consideration"'
        ],
        "Location terms": [
            '"Michigan"', '"Minnesota"'
        ]
    }
    
    all_passed = True
    for category, terms in checks.items():
        print(f"\n{category}:")
        for term in terms:
            if term in google_dork:
                print(f"  ✓ {term}")
            else:
                print(f"  ✗ MISSING: {term}")
                all_passed = False
    
    print("\n" + "=" * 80)
    if all_passed:
        print("🎉 SUCCESS: All checks passed! Dork is extensive and comprehensive.")
    else:
        print("⚠️  WARNING: Some components missing. Review output above.")
    print("=" * 80)
    
    # Compare structure to example
    print("\n📊 STRUCTURE COMPARISON:")
    print("-" * 80)
    print("Expected structure:")
    print("1. (intext:X OR inurl:X OR ... for grant + identity terms)")
    print("2. Quoted identity qualifications")
    print("3. Process terms with wildcards")
    print("4. Location terms")
    print()
    print("Your dork structure matches this format!" if all_passed else "Review structure above")
    print("-" * 80)
    
    return all_passed


def test_non_identity_topic():
    """Test dork generation for non-identity topics (e.g., education, healthcare)."""
    
    print("\n\n" + "=" * 80)
    print("Testing Dork Generation for General Topic (Education Technology)")
    print("=" * 80)
    
    dorks = GrantDorkGenerator.generate_all_dorks(
        topic="education technology",
        location="California, New York"
    )
    
    google_dork = dorks['google']
    
    print("\n📋 GOOGLE DORK OUTPUT:")
    print("-" * 80)
    print(google_dork)
    print("-" * 80)
    
    # Verify components
    checks = [
        "intext:grant", "inurl:grant",
        '"education technology"',
        '"our grant ** process"',
        '"California"', '"New York"'
    ]
    
    print("\n✅ VERIFICATION:")
    all_found = True
    for term in checks:
        if term in google_dork:
            print(f"  ✓ {term}")
        else:
            print(f"  ✗ MISSING: {term}")
            all_found = False
    
    return all_found


if __name__ == '__main__':
    print("\n🚀 EXTENSIVE DORK GENERATOR TESTING\n")
    
    test1_passed = test_indigenous_extensive_dork()
    test2_passed = test_non_identity_topic()
    
    print("\n\n" + "=" * 80)
    print("FINAL RESULTS:")
    print("=" * 80)
    print(f"Indigenous/Tribal Test: {'✅ PASS' if test1_passed else '❌ FAIL'}")
    print(f"General Topic Test: {'✅ PASS' if test2_passed else '❌ FAIL'}")
    print("=" * 80)
