from pyquery import PyQuery as querySelector
class Web_Crawler():
	def __init__(self):
		pass
	def query_First(self, prodname):
		url_name = "http://www.shopping.com/clothing/products?KW=%s" %(prodname)
		try:
			data = querySelector(url = url_name)
			pglst = data('[class = "paginationNew"] a')
			pglst = [int(each.split("PL")[1]) for each in pglst if each.isdigit()]
			pglst.sort()
                       		min_pgno = pglst[0] if pglst else -1
			max_pgno = pglst[-1] if pglst else -1
		except:
			print "URL open Error"
				
		total = 0
		# for each page how many products
		for i in range(min_pgno, max_pgno+1):
			url_name = "http://www.shopping.com/clothing/products~PG-%s?KW=%s" %(str(i), prodname)
			prod_lst = data('[class="dealImage "]')
			total +=  len(prod_lst)
		return total
	def query_Second(self, prodname, pgno):
		try:
			url_name = "http://www.shopping.com/clothing/products~PG-%s?KW=%s" %(str(pgno), prodname)
			prod_lst = data('[class="dealImage "]')
			return len(prod_lst)
		except Exception:
			print "URL open error"
		
	
