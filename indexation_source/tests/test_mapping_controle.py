"""
This module tests mapping_controle
"""
import unittest
from indexation_source.indexation.mapping.mapping_controle import corrige_date_oeie_avis


class TestMappingControle(unittest.TestCase):
    """
    This class tests mapping_controle
    """
    def test_corrige_date_oeie_avis(self):

        assert corrige_date_oeie_avis("1970/07/04") is None
        assert corrige_date_oeie_avis("2018/07/04") == "2018-07-04"
        assert corrige_date_oeie_avis("2018 07 04") == "2018T07T04"


if __name__ == '__main__':
    unittest.main()
