from src.degiro import CSVFileReader
from src.language.language import Languages


class LanguageDetector:

    def getLanguageFromHeader(csvHeader: str):
        if csvHeader == CSVFileReader.CSV_HEADER_NL:
            return Languages.NL
        else:
            raise ValueError(f"The header '{csvHeader}' cannot be managed")
