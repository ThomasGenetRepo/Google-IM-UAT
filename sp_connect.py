# type: ignore
import yaml
from dotenv import load_dotenv, dotenv_values
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

# ctx = ClientContext(site).with_credentials(UserCredential("thomas.genet@mosaic.com", "$$Strawberry22"))
# web = ctx.web
# ctx.load(web)
# ctx.execute_query()
# print("Web title: {0}".format(web.properties['Title']))
# available_methods = dir(web)
# for m in available_methods:
#     print(m)
config_fpath = dotenv_values()['config_fpath']
with open(config_fpath, 'r') as f:
    config = yaml.safe_load(f)
username = config['username']
password = config['password']
site = config['site']

ctx = ClientContext(site).with_credentials(UserCredential(username, password))
t = ctx.web.get_list_item(site)
# ctx.load(web)
# ctx.execute_query()
# print("Web title: {0}".format(web.properties['Title']))