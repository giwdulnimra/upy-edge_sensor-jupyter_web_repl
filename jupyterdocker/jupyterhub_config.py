from dockerspawner import DockerSpawner
from nativeauthenticator import NativeAuthenticator

c.JupyterHub.authenticator_class = NativeAuthenticator
c.JupyterHub.log_level = "DEBUG"
c.JupyterHub.hub_ip = "0.0.0.0"
c.JupyterHub.spawner_class = DockerSpawner
c.JupyterHub.db_url = "sqlite:///data/jupyterhub.sqlite"

c.DockerSpawner.network_name = "jupyterhub"
c.DockerSpawner.remove = True
c.DockerSpawner.volumes = {"jupyterhub-user-{username}": "/home/jovyan/work"}
c.DockerSpawner.notebook_dir = "/home/jovyan/work"
c.DockerSpawner.image = "jupyter/datascience-notebook:latest"
c.DockerSpawner.http_timeout = 300

c.GenericOAuthenticator.enable_auth_state = True
c.Authenticator.admin_users = {"admin"}
c.Authenticator.allowed_users = set()
c.NativeAthenticator.open_signup = True
c.NativeAthenticator.create_system_users = True
