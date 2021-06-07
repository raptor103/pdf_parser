import sys
sys.path.append("..")
from PDF_parser import SuperKeywordFinder


def test_get_list_of_key_words():
    kf = SuperKeywordFinder('keywords_for_tests.txt')
    output = kf.get_list_of_key_words()
    assert sorted(output) == sorted(['zarovka', 'router', 'severe', 'cz', '75', 'klavesnice', 'sluchatka', 'vacsinu', 'mys', 'pocitac', 'mobil', 'kocka', 'neskor', 'polskom', 'povodnou', 'kolo', 'auto', 'slon', 'talirek'])

def test_output_of_program():
    kf = SuperKeywordFinder('keywords_for_pdf_search_test.txt')
    pdfs, pdf_total_matches, pdf_matches = kf.main()
    assert sorted(pdfs) == sorted(['pdf_test1.pdf', 'pdf_test2.pdf', 'pdf_test3.pdf', 'pdf_test4.pdf'])
    assert pdf_total_matches == {'pdf_test1.pdf': 135, 'pdf_test2.pdf': 110, 'pdf_test3.pdf': 30, 'pdf_test4.pdf': 56}
    assert pdf_matches == {'pdf_test1.pdf': {'hi': 4, 'sdeleni': 12, 'erdomed': 2, 'ranitidine': 2, 'pms': 3, 'registr': 83, 'lite': 2, 'dulezita': 6, 'programu': 21}, 'pdf_test2.pdf': {'hi': 14, 'sdeleni': 9, 'dalacin': 1, 'registr': 73, 'dulezita': 5, 'programu': 8}, 'pdf_test3.pdf': {'hi': 2, 'atomoxetin': 24, 'niekolkych': 1, 'lite': 2, 'programu': 1}, 'pdf_test4.pdf': {'lite': 3, 'registr': 1, 'ezetimib': 11, 'hi': 41}}

