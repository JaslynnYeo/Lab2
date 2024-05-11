import Lab2 
import statistics
def test_find_min_max():
    commno_list = [5, 67, 320]
    test_arr = [5, 320]
    min_max_list = [min(commno_list), max(commno_list)]
    assert ( min_max_list == test_arr)

def test_calc_average():
    commno_list = [5, 67, 320]
    test_arr = 392/3
    avg = Lab2.calc_avg(commno_list)
    assert (avg == test_arr)

def test_calc_median_temperature(): 
    sorted_list = [2, 5, 6, 1, 8] 
    median = Lab2.calc_median(sorted_list)
    test_arr = 5
    assert (median == test_arr)

