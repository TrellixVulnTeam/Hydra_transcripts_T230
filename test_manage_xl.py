import hydra_ts
import unittest

class TestResults(unittest.TestCase):

	titles = ( 'Pfam Domains',
				'Pfam domains in predicted Hydra proteins'
			 )

	def create_excel(self):
		# Creates a new spreadsheet with header based on website and current date
		for title,subtitle in self.create_excel: 
			result = create_excel.create_header(term)
			self.assertEqual(value,result, "Should be geneID: " +value)


if __name__ == '__main__':
	unittest.main()