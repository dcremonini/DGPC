from unittest import TestCase

import pytest

from src.csvparser.csvparser import LanguageDetector
from src.degiro import CSVFileReader
from src.language.language import Languages


class TestLanguageDetector(TestCase):

    def test_urecognized_header_should_raise(self):
        with pytest.raises(ValueError, match=r"The header 'THIS_IS_A_NON_MANAGED_HEADER' cannot be managed" ):
            LanguageDetector.getLanguageFromHeader("THIS_IS_A_NON_MANAGED_HEADER") == "DON'T_CARE_VALUE"

    def test_get_NL_language_from_header(self):
        assert LanguageDetector.getLanguageFromHeader(
            CSVFileReader.CSV_HEADER_NL) == Languages.NL, "The Dutch header is not recognized as NL"
