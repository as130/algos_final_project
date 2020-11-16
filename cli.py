import click
import pickle
import numpy as np
FILENAME = 'trained_knn.sav'

# load the model from disk
@click.command()

## TODO: fill in help section
@click.option('--black', prompt='black', type=int)
@click.option('--population', prompt='The population of the county',
              help='The person to greet.', type=int)
@click.option('--poverty', prompt='poverty', type=int)
@click.option('--men', prompt='men', type=int)
@click.option('--women', prompt='women', type=int)
@click.option('--white', prompt='white', type=int)
@click.option('--native', prompt='native', type=int)
@click.option('--hispanic', prompt='hispanic', type=int)
@click.option('--asian', prompt='asian', type=int)
@click.option('--pacific',prompt='pacific', type=int)
@click.option('--income', prompt='income',type=int)
@click.option('--drive', prompt='drive', type=int)
@click.option('--walk', prompt='walk', type=int)
@click.option('--transit', prompt='transit', type=int)
@click.option('--professional', prompt='professional', type=int)
@click.option('--work_at_home', prompt='work_at_home', type=int)
@click.option('--unemployment', prompt='unemployment', type=int)
@click.option('--selfemployed', prompt='selfemployed', type=int)
@click.option('--employed', prompt='employed', type=int)
def cli(black, population, poverty, men, women, white, native, hispanic, 
        asian, pacific, income, drive, walk, transit, professional, work_at_home, 
       unemployment, selfemployed, employed) :
    loaded_model = pickle.load(open(FILENAME, 'rb'))
    X = [black, population, poverty, men, women, white, native, hispanic, 
        asian, pacific, income, drive, walk, transit, professional, work_at_home, 
       unemployment, selfemployed, professional, employed]
    X = np.asarray(X, dtype=np.float32)
    X_test = np.array([X])
    result = loaded_model.predict(X_test)
    print(result)
    print(black, population, poverty, men, women, white, native, hispanic, 
        asian, pacific, income, drive, walk, transit, professional, work_at_home, 
       unemployment, selfemployed, professional, employed)

if __name__ == '__main__':
    cli()