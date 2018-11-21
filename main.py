""" Main Module """

import logging

# pylint: disable=import-error
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

LOGGING = logging.getLogger(__name__)

MENU = [
    ExtensionResultItem(icon='images/icon.png',
                        name='Projects',
                        description='Open Projects page',
                        on_enter=OpenUrlAction("https://cloud.digitalocean.com/projects")),
    ExtensionResultItem(icon='images/icon.png',
                        name='Droplets',
                        description='Open Droplets page',
                        on_enter=OpenUrlAction("https://cloud.digitalocean.com/droplets")),
    ExtensionResultItem(icon='images/icon.png',
                        name='Spaces',
                        description='Open Spaces page',
                        on_enter=OpenUrlAction("https://cloud.digitalocean.com/spaces")),
    ExtensionResultItem(icon='images/icon.png',
                        name='Kubernetes',
                        description='Open Kubernetes',
                        on_enter=OpenUrlAction("https://cloud.digitalocean.com/kubernetes")),
    ExtensionResultItem(icon='images/icon.png',
                        name='Billing',
                        description='Open Billing page',
                        on_enter=OpenUrlAction("https://cloud.digitalocean.com/account/billing")),
    ExtensionResultItem(icon='images/icon.png',
                        name='Service Status',
                        description='Open DigitalOcean status page',
                        on_enter=OpenUrlAction("https://status.digitalocean.com/"))
]


class DigitalOceanExtension(Extension):
    """ Main Extension Class  """

    def __init__(self):
        """ Initializes the extension """
        super(DigitalOceanExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles keyboard event """
        return RenderResultListAction(MENU)


if __name__ == '__main__':
    DigitalOceanExtension().run()
