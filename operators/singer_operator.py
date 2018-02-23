import json

from airflow.operators.bash_operator import BashOperator
from airflow.utils.decorators import apply_defaults


class SingerOperator(BashOperator):
    """
    Singer Plugin

    :param tap:            The relevant Singer Tap.
    :type tap:             string
    :param target:         The relevant Singer Target
    :type target:          string
    :param tap_config:     The config path for the Singer Tap.
    :type tap_config:      string
    :param target_config:  The config path for the Singer Target.
    :type target_config:   string
    """

    @apply_defaults
    def __init__(self,
                 tap,
                 target,
                 tap_config=None,
                 target_config=None,
                 *args,
                 **kwargs):

        self.tap = "tap-{}".format(tap)
        self.target = "target-{}".format(target)
        self.tap_config = tap_config
        self.target_config = target_config

        if self.tap_config:
            if self.target_config:
                self.bash_command = "{} -c {} | {} -c {}".format(self.tap,
                                                                 self.tap_config,
                                                                 self.target,
                                                                 self.target_config)
            else:
                self.bash_command = "{} -c {} | {}".format(self.tap,
                                                           self.tap_config,
                                                           self.target)
        elif self.target_config:
            self.bash_command = "{} | {} -c {}".format(self.tap,
                                                       self.target,
                                                       self.target_config)
        else:
            self.bash_command = "{} | {}".format(self.tap,
                                                 self.target)

        super().__init__(bash_command=self.bash_command, *args, **kwargs)
