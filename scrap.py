import re, time, os
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

print("teste")

# Web Scraping da página Viva Real
# Criação do DataFrame
df = pd.DataFrame(columns=['Endereço', 'Bairro', 'Cidade', 'Estado', 'CEP', 'Preço', 'Condomínio', 'IPTU', 'Área', 'Quartos', 'Banheiros', 'Vagas', 'Descrição', 'Link'])

# Criação do driver do Selenium


driver = webdriver.Chrome()


# Loop para percorrer as páginas

for i in range(1, 2):

    # URL da página
    url = 'https://www.vivareal.com.br/venda/sp/sao-paulo/zona-sul/?pagina=' + str(i)

    # Acessa a página
    driver.get(url)

    # Pausa de 5 segundos para carregar a página
    time.sleep(5)

    # Obtém o código HTML da página
    html = driver.page_source

    # Criação do objeto BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Obtém os imóveis da página
    imoveis = soup.find_all('article', class_='property-card__container js-property-card')

    # Loop para percorrer os imóveis
    for imovel in imoveis:

        # Obtém o endereço
        endereco = imovel.find('span', class_='property-card__address').getText()

        # Obtém o bairro
        bairro = imovel.find('span', class_='property-card__address').getText()

        # Obtém a cidade
        cidade = imovel.find('span', class_='property-card__address').getText()

        # Obtém o estado
        estado = imovel.find('span', class_='property-card__address').getText()

        # Obtém o CEP
        cep = imovel.find('span', class_='property-card__address').getText()

        # Obtém o preço
        preco = imovel.find('div', class_='property-card__price js-property-card-prices js-property-card__price-small').getText()

        # Obtém o condomínio
        condominio = imovel.find('strong', class_='js-condo-price').getText()

        # Obtém o IPTU
        iptu = imovel.find('strong', class_='js-condo-price').getText()

        # Obtém a área
        area = imovel.find('li', class_='property-card__detail-item property-card__detail-area js-property-card-detail-area').getText()

        # Obtém o número de quartos
        quartos = imovel.find('li', class_='property-card__detail-item property-card__detail-room js-property-detail-rooms').getText()

        # Obtém o número de banheiros
        banheiros = imovel.find('li', class_='property-card__detail-item property-card__detail-bathroom js-property-detail-bathroom').getText()

        # Obtém o número de vagas
        vagas = imovel.find('li', class_='property-card__detail-item property-card__detail-garage js-property-detail-garages').getText()

        # Obtém a descrição
        descricao = imovel.find('div', class_='property-card__description js-property-card-description').getText()

        # Obtém o link

        link = imovel.find('a', class_='property-card__content-link js-card-title').get('href')

        # Adiciona os dados no DataFrame

        df.loc[len(df)] = [endereco, bairro, cidade, estado, cep, preco, condominio, iptu, area, quartos, banheiros, vagas, descricao, link]

# Fecha o driver

driver.quit()

# Salva os dados em um arquivo CSV

df.to_csv('imoveis.csv', index=False, sep=';', encoding='utf-8-sig')

# Imprime o DataFrame

print(df)

# Imprime o DataFrame

print(df.head())

