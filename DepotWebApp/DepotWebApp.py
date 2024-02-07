"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from DepotWebApp.Pages.index import *
from DepotWebApp.Pages.depot_select import *
from DepotWebApp.Pages.managment_site import *


# Create app instance and add index page.
app = rx.App()
app.add_page(index)
app.add_page(depot_select_page)
app.add_page(managment_site)