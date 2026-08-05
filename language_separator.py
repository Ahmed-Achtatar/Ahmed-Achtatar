import re

def split_french_arabic(text):
    """
    Splits a string containing both French and Arabic text into two separate strings.

    Args:
        text (str): The input string containing mixed text.

    Returns:
        dict: A dictionary with 'french' and 'arabic' keys.
    """
    if not text:
        return {'french': '', 'arabic': ''}

    # Regex for Arabic characters (including some supplements for wide coverage)
    # \u0600-\u06FF: Arabic
    # \u0750-\u077F: Arabic Supplement
    # \u08A0-\u08FF: Arabic Extended-A
    # \uFB50-\uFDFF: Arabic Presentation Forms-A
    # \uFE70-\uFEFF: Arabic Presentation Forms-B
    arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]+')

    # Extract Arabic parts
    arabic_parts = arabic_pattern.findall(text)
    arabic_text = ' '.join(arabic_parts).strip()

    # Remove Arabic parts from the original text to get French/Latin
    # We also replace the arabic chars with space to avoid merging french words if they were adjacent
    french_text = arabic_pattern.sub(' ', text)

    # Clean up the French text
    # Remove common separators that might be left over: () - / | [ ]
    # We replace them with space, then normalize whitespace
    french_text = re.sub(r'[()\[\]\-/|]', ' ', french_text)

    # Normalize whitespace (replace multiple spaces with single space and strip)
    french_text = ' '.join(french_text.split())

    return {
        'french': french_text,
        'arabic': arabic_text
    }

if __name__ == "__main__":
    test_cases = [
        "Produit (منتج)",
        "Catégorie - فئة",
        "Homme / رجل",
        "Téléphone 123 (هاتف 123)",
        "Just French",
        "فقط عربي"
    ]

    print(f"{'Original':<30} | {'French':<20} | {'Arabic':<20}")
    print("-" * 76)

    for case in test_cases:
        result = split_french_arabic(case)
        print(f"{case:<30} | {result['french']:<20} | {result['arabic']:<20}")
