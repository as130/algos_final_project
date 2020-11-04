import click
import pickle
import numpy as np
FILENAME = 'trained_knn.sav'

# load the model from disk
@click.command()

## TODO: fill in help section
@click.option('--black', prompt='Percentage of population that is black', type=int)
@click.option('--population', prompt='The population of the county', type=int)
@click.option('--poverty', prompt='Percentage under poverty level', type=int)
@click.option('--men', prompt='Number of men', type=int)
@click.option('--women', prompt='Number of women', type=int)
@click.option('--white', prompt='Percentage of population that is white', type=int)
@click.option('--native', prompt='Percentage of population that is Native American or Native Alaskan', type=int)
@click.option('--hispanic', prompt='Percentage of population that is Hispanic/Latino', type=int)
@click.option('--asian', prompt='Percentage of population that is Asian', type=int)
@click.option('--pacific',prompt='Percentage of population that is Native Hawaiian or Pacific Islander', type=int)
@click.option('--income', prompt='Median household income ($)',type=int)
@click.option('--drive', prompt='Percentage commuting alone in a car, van, or truck', type=int)
@click.option('--walk', prompt='Percentage walking to work', type=int)
@click.option('--transit', prompt='Percentage commuting on public transportation', type=int)
@click.option('--professional', prompt='Percentage employed in management, business, science, and arts', type=int)
@click.option('--work_at_home', prompt='Percentage working at home', type=int)
@click.option('--unemployment', prompt='unemployment rate (as a percentage)', type=int)
@click.option('--selfemployed', prompt='Percentage self-employed', type=int)
@click.option('--employed', prompt='Number of employed (16+)', type=int)
def cli(black, population, poverty, men, women, white, native, hispanic, 
        asian, pacific, income, drive, walk, transit, professional, work_at_home, 
       unemployment, selfemployed, employed) :
    click.echo(click.style('Thinking...', blink=True, fg='cyan'))
    loaded_model = pickle.load(open(FILENAME, 'rb'))
    X = [black, population, poverty, men, women, white, native, hispanic, 
        asian, pacific, income, drive, walk, transit, professional, work_at_home, 
       unemployment, selfemployed, professional, employed]
    X = np.asarray(X, dtype=np.float32)
    X_test = np.array([X])
    result = loaded_model.predict(X_test)
    click.echo(click.style('Prediction:', fg='red', underline=True))
    if result == 0.0 :
      click.echo(click.style("25th percentile or below", fg='green'))
    if result == 1.0:
      click.echo(click.style("50th percentile or below", fg='green'))
    if result == 2.0:
      click.echo(click.style("75th percentile or below", fg='green'))
    if result == 3.0:
      click.echo(click.style("99th percentile or below", fg='green'))

if __name__ == '__main__':
    cli()