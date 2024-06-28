import os



def list_pages():
    pages = os.listdir(f'{os.getcwd()}/Wiki_Pages')


    pages = [page.removesuffix('.txt') for page in pages]
    return pages


def get_page(page):
    pages = os.listdir(f'{os.getcwd()}/Wiki_Pages')
    page = f'{page}.txt'

    if not page in pages:
        return False
    
    with open(f'{os.getcwd()}/Wiki_Pages/{page}') as f:
        data= f.read()

    return data
    

if __name__ == "__main__":
    print(list_pages())