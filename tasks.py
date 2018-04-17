# Based on https://github.com/jupyterlab/jupyterlab-demo/blob/master/tasks.py

import os
from shutil import which

from invoke import task, Collection

env_name = 'jupyter-demo'
source = '' if os.name == 'nt' else 'source'


@task
def environment(ctx, clean=False, env_name=env_name):
    '''
    Creates environment for demo
    Args:
    clean: deletes environment prior to reinstallation
    env_name: name of environment to install
    '''
    if clean and env_name != 'root':
        print(f'deleting environment {env_name}')
        ctx.run(f'{source} deactivate && conda env remove -n {env_name}')
        
    # Create a new environment
    print(f'creating environment {env_name}')
    ctx.run(f'conda env create -n {env_name}')

    build(ctx, env_name=env_name)


@task
def build(ctx, env_name=env_name):
    '''
    Builds an environment with appropriate extensions.
    '''    
    cmd_str = ' && '.join(str for str in [
        f'{source} activate {env_name}' if env_name != 'root' else None,
        'jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.33',
        'jupyter labextension install beakerx-jupyterlab',
        'jupyter labextension install bqplot',
        'jupyter lab clean',
        'jupyter lab build'
        ] if str)
    
    print(f'> {cmd_str}')
    ctx.run(cmd_str)


@task
def clean(ctx, env_name=env_name):
    '''
    Removes environment for demo
    Args:
    env_name: name of environment to install
    '''
    if env_name != 'root':
        print(f'deleting environment {env_name}')
        ctx.run(f'{source} deactivate && conda env remove -n {env_name}')


# Configure cross-platform settings.
ns = Collection(environment, build, clean)
ns.configure({
    'run': {
        'shell': which('bash') if os.name != 'nt' else which('cmd'),
        'pty': False if os.name == 'nt' else True
    }
})
