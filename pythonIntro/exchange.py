import httpx
input_value = float(input('Zadejte castku CZK pro prevod: '))
target_currency = input('Zadejte cilovou menu: ')


r = httpx.get('https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?')
rates_str = r.text

rates_list = rates_str.split('\n')

target_rate_str = None
for rate_item in rates_list:
    if target_currency in rate_item:
        target_rate_str = rate_item

if not target_rate_str:
    print('Zadaná čísla nenalezena ')
    exit()

rate = float(target_rate_str.split('|')[-1].replace(',', '.'))

output_value = input_value/rate

print(f"Prevedena castka {output_value:.2f} {target_currency}")


