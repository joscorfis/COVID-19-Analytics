from dateutil.tz import UTC
from django.test import TestCase
from main import queries
from datetime import datetime,timedelta
import unittest

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.management import call_command
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCases(TestCase):

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_basico(self):
        self.assertEqual(5,5)

    def test_run_query(self):
        test_query = """
        {
            search(query: "topic:covid-19", type: REPOSITORY, first: 100) {
                repositoryCount
            }
        }
        """
        result = queries.run_query(test_query)
        self.assertEqual(type(result),type({}))
        self.assertTrue(int(result["data"]["search"]["repositoryCount"])>4000)


    def test_get_repositorios_coronavirus_mas_visualizados(self):
        result = queries.get_repositorios_coronavirus_mas_seguidores()
        self.assertEquals(type(result[0][0]),type(''))
        self.assertEquals(type(result[1][0]),type(''))
        self.assertEquals(type(result[2][0]),type(''))
        self.assertEquals(type(result[3][0]),type(int()))
        self.assertEquals(type(result[4][1]),type(float()))
        self.assertTrue(50<=len(result[1])<=100)
        

    def test_get_repositorios_coronavirus_mas_forks(self):
        result = queries.get_repositorios_coronavirus_mas_forks()
        self.assertEquals(type(result[0][0]),type(''))
        self.assertEquals(type(result[1][0]),type(''))
        self.assertEquals(type(result[2][0]),type(''))
        self.assertEquals(type(result[3][0]),type(int()))
        self.assertEquals(type(result[4][1]),type(float()))
        self.assertTrue(50<=len(result[1])<=100)


    def test_get_repositorios_coronavirus_mas_estrellas(self):
        result = queries.get_repositorios_coronavirus_mas_estrellas()
        self.assertEquals(type(result[0][0]),type(''))
        self.assertEquals(type(result[1][0]),type(''))
        self.assertEquals(type(result[2][0]),type(''))
        self.assertEquals(type(result[3][0]),type(int()))
        self.assertEquals(type(result[4][1]),type(float()))
        self.assertTrue(50<=len(result[1])<=100)


    def test_get_lenguajes_mas_utilizados(self):
        result = queries.get_lenguajes_mas_utilizados()
        self.assertEquals(type(result[0]),type(''))
        self.assertTrue(20<=len(set(result))<=50)
        self.assertTrue('Python' in result)


    def test_get_primeros_repositorios_coronavirus_creados(self):
        result = queries.get_primeros_repositorios_coronavirus_creados()
        self.assertEquals(type(result[0][0]),type(''))
        self.assertEquals(type(result[1][0]),type(''))
        self.assertEquals(type(result[2][0]),type(''))
        self.assertEquals(type(result[3][0]),type(int()))
        self.assertTrue(queries.str_to_datetime(result[2][0])<datetime.now() and queries.str_to_datetime(result[2][0])>datetime(2019,12,30))
        self.assertTrue(80<=len(result[1])<=100)


    def test_get_repositorios_coronavirus_mas_actualizados(self):
        result = queries.get_repositorios_coronavirus_mas_actualizados()
        self.assertEquals(type(result[0][0]),type(''))
        self.assertEquals(type(result[1][0]),type(''))
        self.assertTrue(queries.str_to_datetime(result[2][0])<datetime.now() and queries.str_to_datetime(result[2][0])>datetime(2019,12,30))
        self.assertTrue(queries.str_to_datetime(result[3][0])<datetime.now() and queries.str_to_datetime(result[3][0])>(datetime.now()-timedelta(hours=48)))
        self.assertEquals(type(result[4][1]),type(''))
        self.assertTrue(queries.str_to_datetime(result[5][0])<datetime.now() and queries.str_to_datetime(result[5][0])>(datetime.now()-timedelta(hours=48)))
        self.assertEquals(type(result[6][0]),type(''))
        self.assertEquals(type(result[7]),type(zip()))
        self.assertTrue(50<=len(result[1])<=100)


    def test_get_evolucion_repositorios_coronavirus(self):
        result = queries.get_evolucion_repositorios_coronavirus([],"2019-12-30")
        self.assertEquals(type(result[0][0]),type(''))
        self.assertTrue(queries.str_to_datetime(result[1][0])<datetime.now() and queries.str_to_datetime(result[1][0])>datetime(2019,12,30))
        self.assertEquals(type(result[2][0]),type(int()))
        self.assertEquals(type(result[3][0]),type(''))
        self.assertEquals(type(result[4][1]),type([]))
        self.assertTrue(500<=len(result[1])<=2000)


    def test_get_repositorios_coronavirus_mas_proyectos(self):
        result = queries.get_repositorios_coronavirus_mas_proyectos([],"2019-12-31T00:00:00+00:00")
        self.assertEquals(type(result[0][0]),type(''))
        self.assertEquals(type(result[1][0]),type(''))
        self.assertTrue(queries.str_to_datetime(result[2][0])<datetime.now() and queries.str_to_datetime(result[2][0])>datetime(2019,12,30))
        self.assertEquals(type(result[3][0]),type([]))
        self.assertEquals(type(result[4][1]),type(int()))
        self.assertTrue(15<=len(result[1])<=100)


    def test_get_information_from_repository(self):
        result = queries.get_information_from_repository("COVID-19","CSSEGISandData")
        self.assertEquals(type(result),type([]))
        self.assertEquals(type(result[0]),type(''))
        self.assertEquals(type(result[1]),type(''))
        self.assertEquals(type(result[2]),type(''))
        self.assertEquals(type(result[3]),type(''))
        self.assertEquals(type(result[4]),type(''))
        self.assertEquals(type(result[5]),type(''))
        self.assertEquals(type(result[6]),type([]))
        self.assertEquals(type(result[7]),type([]))
        self.assertEquals(type(result[8]),type(int()))
        self.assertEquals(type(result[9]),type([]))
        self.assertTrue(queries.str_to_datetime(result[10])<datetime.now() and queries.str_to_datetime(result[10])>datetime(2019,12,30))
        self.assertTrue(queries.str_to_datetime(result[11])<datetime.now() and queries.str_to_datetime(result[11])>datetime(2019,12,30))
        self.assertEquals(type(result[12]),type(int()))
        self.assertEquals(type(result[13]),type(int()))
        self.assertEquals(type(result[14]),type(int()))
        self.assertEquals(type(result[15]),type(''))
        self.assertTrue(queries.str_to_datetime(result[16])<datetime.now() and queries.str_to_datetime(result[16])>datetime(2019,12,30))
        self.assertEquals(type(result[17]),type(''))


    def test_get_paises_mas_repositorios(self):
        result = queries.get_paises_mas_repositorios()
        self.assertEquals(type(result[0]),type(''))
        self.assertTrue(10<=len(set(result))<=40)
        self.assertTrue('Italia' in result)
        
    def test_get_cifras_pandemia(self):
        result = queries.get_cifras_pandemia()
        self.assertEquals(type(result),type([]))
        self.assertEquals(type(result[0]),type(int()))
        self.assertTrue(result[0]<7902341768)
        self.assertEquals(type(result[1]),type(int()))
        self.assertTrue(result[1]<7902341768)
        self.assertEquals(type(result[2]),type(int()))
        self.assertTrue(result[2]<7902341768)


    # ---


class TestSelenium(StaticLiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome("C:\Program Files\chromedriver", options=options)
        self.driver.set_window_size(1280, 720)
        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.driver.quit()
  
    def test_consultar_repositorios_con_mas_seguidores(self):
        self.driver.get("http://localhost:8000/")
        self.driver.find_element(By.XPATH, "//button[contains(.,\'Repositorios COVID con más seguidores/watchers\')]").click()
        elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Repositorios COVID con más seguidores/watchers\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Seguidores\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.LINK_TEXT, "COVID-19")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.ID, "chart")
        assert len(elements) > 0

    def test_consultar_repositorios_con_mas_forks(self):
        self.driver.get("http://localhost:8000/")
        self.driver.find_element(By.CSS_SELECTOR, ".col-sm-6 > .invertir_colores:nth-child(1) > div").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".text-center > b")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, "tr:nth-child(1) > .text-center:nth-child(1)")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.LINK_TEXT, "COVID-19")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.ID, "chart")
        assert len(elements) > 0

    def test_consultar_repositorios_con_mas_estrellas(self):
        self.driver.get("http://localhost:8000/")
        self.driver.find_element(By.CSS_SELECTOR, ".invertir_colores:nth-child(3) b").click()
        elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Repositorios COVID con más estrellas\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Estrellas\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.LINK_TEXT, "COVID-19")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.ID, "chart")
        assert len(elements) > 0

    def test_consultar_lenguajes_de_programacion_mas_utilizados(self):
        self.driver.get("http://localhost:8000/")
        self.driver.find_element(By.CSS_SELECTOR, ".fila-del-centro:nth-child(1) > div").click()
        elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Lenguajes más utilizados en los repositorios COVID del top 100\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Lenguaje\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Repositorios que lo utilizan\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.ID, "chart")
        assert len(elements) > 0
  
    def test_consultar_repositorios_que_aparecieron_primero(self):
        self.driver.get("http://localhost:8000/")
        self.driver.find_element(By.XPATH, "//button[contains(.,\'Repositorios COVID que aparecieron primero\')]").click()
        elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Repositorios COVID que aparecieron primero\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Tiempo\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Fecha de creación\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.ID, "chart")
        assert len(elements) > 0

    def test_consultar_repositorios_mas_actualizados(self):
        self.driver.get("http://localhost:8000/")
        self.driver.find_element(By.CSS_SELECTOR, ".fila-del-centro:nth-child(3)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".tablinks:nth-child(1)").text == "Por modificación"
        self.driver.find_element(By.CSS_SELECTOR, "#Updates > .text-center").click()
        elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Repositorios COVID con modificaciones más recientes\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Última modificación\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Hace...\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.ID, "chart")
        assert len(elements) > 0
        self.driver.find_element(By.CSS_SELECTOR, ".tablinks:nth-child(2)").click()
        assert self.driver.find_element(By.XPATH, "//button[contains(.,\'Por commits\')]").text == "Por commits"
        elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Repositorios COVID con commits más recientes\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Último commit\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, "#Commits tr:nth-child(1) > .text-center:nth-child(2)")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".rotateimg")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.ID, "chart2")
        assert len(elements) > 0

    def test_consultar_repositorios_con_mas_proyectos(self):
        self.driver.get("http://localhost:8000/")
        self.driver.find_element(By.CSS_SELECTOR, ".col-sm-6:nth-child(1) > .espaciado:nth-child(1) > div").click()
        elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Repositorios COVID con más proyectos\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Nº de proyectos\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Proyectos\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.LINK_TEXT, "Bmore-Responsive")
        assert len(elements) > 0
    
    def test_consultar_paises_con_mas_repositorios(self):
        self.driver.get("http://localhost:8000/")
        self.driver.find_element(By.CSS_SELECTOR, ".col-sm-6:nth-child(1) > .espaciado:nth-child(3) > div").click()
        elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Países más activos en la creación de repositorios COVID del top 100\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'País\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Repositorios que contienen\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.ID, "chart")
        assert len(elements) > 0

    def test_representar_repositorios_que_han_ido_apareciendo(self):
        self.driver.get("http://localhost:8000/")
        self.driver.find_element(By.XPATH, "//button[contains(.,\'Representación del número de repositorios COVID que han ido apareciendo con el tiempo\')]").click()
        elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Representación del número de repositorios COVID que han ido apareciendo con el tiempo\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//h3[contains(.,\'Tabla resumen de resultados\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Año / Mes\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//h3[contains(.,\'Gráfica de linea\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.ID, "chart")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//h3[contains(.,\'Tabla con todos los repositorios COVID\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'ID\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Nombre\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Propietario\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Fecha de creación\')]")
        assert len(elements) > 0

    def test_get_information_from_repository(self):
        self.driver.get("http://localhost:8000/")
        self.driver.find_element(By.CSS_SELECTOR, ".row > .invertir_colores").click()
        self.driver.find_element(By.LINK_TEXT, "COVID-19").click()
        elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'URL del repositorio:\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Fecha de creación:\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Descripción\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Propietario\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Localidad\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'¿Es un fork de otro repositorio?\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Labels\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Número de proyectos\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'    Proyectos\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Fecha de último push\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Fecha de última modificación\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Número de seguidores\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Número de estrellas\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Número de forks que se le han hecho\')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//th[contains(.,\'Lenguajes\')]")
        assert len(elements) > 0

    def test_consultar_cifras_pandemia(self):
        self.driver.get("http://localhost:8000/")
        elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Contagiados: \')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Recuperados: \')]")
        assert len(elements) > 0
        elements = self.driver.find_elements(By.XPATH, "//b[contains(.,\'Fallecidos: \')]")
        assert len(elements) > 0