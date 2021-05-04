from src.degiro import CSVFileReader
from src.language.language import Languages


class LanguageDetector:

    def get_language_from_header(csv_header: str) -> str:
        if csv_header == CSVFileReader.CSV_HEADER_NL:
            return Languages.NL
        else:
            raise ValueError(f"The header '{csv_header}' cannot be managed")
