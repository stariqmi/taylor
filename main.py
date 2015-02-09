from selenium import webdriver
import socket

short = [["Blvd","Bl"], ["Ave", "Av"], ["Street", "St"], ["Pkwy", "Pk"], ["Way", "Wa"]]

def getUrl(driver, address, resultFile, sock):
	driver.get("https://www.invoicecloud.com/portal/(S(wo2ya5qdaac4vfezgvutabzg))/Site.aspx?G=f92bbd52-0986-4971-8f81-6e44801f28d6")

	for sh in short:
		address = address.replace(sh[0], sh[1]);

	try:
		driver.find_element_by_link_text("Real Estate Taxes").click();

		address_field = driver.find_element_by_id("rptInputs_ctl03_txtValue");
		address_field.send_keys(address);
		driver.find_element_by_id("btnSearch").click();

		table = driver.find_element_by_id("dgResults_ctl00");

		for row in table.find_elements_by_tag_name("tr"):
			tds = row.find_elements_by_tag_name("td");
			if len(tds) == 9:
				found = tds[4].text;
				if (found == address.upper()):
					href = tds[8].find_element_by_tag_name("a").get_attribute("href");
					if (href.find("pdf") == -1):
						print(href);
						resultFile.write(href + "\n");
						sock.send(address + "<=>" + href);
	except:
		print("ERROR: Search failed for " + address);

def collectUrls(driver, sock):
	resultFile = open("result.txt","w");
	csv = open("list.csv");
	for line in csv.readlines():
		address = line.split(",")[0];
		getUrl(driver, address, resultFile, sock);
	driver.close();

# Create a socket client
s = socket.socket();
s.connect(("localhost",8080));

driver = webdriver.PhantomJS();
collectUrls(driver, s);
driver.close();