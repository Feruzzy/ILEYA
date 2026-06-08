import unittest
import grade_function

class TestGradeFunction(unittest.TestCase):

    def test_calculate_totals_and_averages_standard(self):
     
        mock_scores = [
            [80.0, 90.0],  
            [50.0, 60.0],  
            [75.0, 75.0]   
        ]
        num_students = 3
        num_subjects = 2
        expected_totals = [170.0, 110.0, 150.0]
        expected_averages = [85.0, 55.0, 75.0]
        
        
        actual_totals, actual_averages = grade_function.calculate_totals_and_averages(
            mock_scores, num_students, num_subjects
        )
        
       
        self.assertEqual((actual_totals, actual_averages), (expected_totals, expected_averages))


    def test_calculate_totals_and_averages_perfect_and_zeros(self):
       
        mock_scores = [
            [100.0, 100.0, 100.0], 
            [0.0, 0.0, 0.0]        
        ]
        num_students = 2
        num_subjects = 3
        expected_totals = [300.0, 0.0]
        expected_averages = [100.0, 0.0]
        
        
        actual_totals, actual_averages = grade_function.calculate_totals_and_averages(
            mock_scores, num_students, num_subjects
        )
        
        
        self.assertEqual((actual_totals, actual_averages), (expected_totals, expected_averages))


    def test_calculate_totals_and_averages_single_student_single_subject(self):
        
        mock_scores = [
            [72.5]  
        ]
        num_students = 1
        num_subjects = 1
        expected_totals = [72.5]
        expected_averages = [72.5]
        
        
        actual_totals, actual_averages = grade_function.calculate_totals_and_averages(
            mock_scores, num_students, num_subjects
        )
        
        
        self.assertEqual((actual_totals, actual_averages), (expected_totals, expected_averages))



