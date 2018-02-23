from airflow.plugins_manager import AirflowPlugin
from singer_plugin.operators.singer_operator import SingerOperator


class SingerPlugin(AirflowPlugin):
    name = "singer_plugin"
    hooks = []
    operators = [SingerOperator]
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []
