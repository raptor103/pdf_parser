import sys
sys.path.append("..")
from PDF_parser import SuperKeywordFinder


def test_get_list_of_key_words():
    kf = SuperKeywordFinder('keywords_for_tests.txt')
    output = kf.get_list_of_key_words()
    assert sorted(output) == sorted(['severe', 'cz-75', 'klavesnice', 'sluchatka', 'vacsinu', 'mys', 'pocitac', 'mobil', 'kocka', 'neskor', 'polskom', 'povodnou', 'kolo', 'auto', 'slon', 'talirek'])


def test_output_of_program():
    kf = SuperKeywordFinder('keywords_for_pdf_search_test.txt')
    pdfs, pdf_total_matches, pdf_matches = kf.main()
    assert sorted(pdfs) == sorted(['pdf_test1.pdf', 'pdf_test2.pdf', 'pdf_test3.pdf'])
    assert pdf_total_matches == {'pdf_test1.pdf': 103, 'pdf_test2.pdf': 88, 'pdf_test3.pdf': 25}
    assert pdf_matches == {'pdf_test1.pdf': {'dulezita': 6, 'registr': 83, 'sdeleni': 12, 'erdomed': 2}, 'pdf_test2.pdf': {'dulezita': 5, 'registr': 73, 'sdeleni': 9, 'dalacin': 1}, 'pdf_test3.pdf': {'niekolkych': 1, 'atomoxetin': 24}}



