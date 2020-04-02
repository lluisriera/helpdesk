# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Helpdesk Project",
    "summary": """
        Helpdesk""",
    "version": "13.0.1.0.0",
    "license": "AGPL-3",
    "category": "After-Sales",
    "author": "AdaptiveCity, "
    "C2i Change 2 Improve, "
    "Domatix, "
    "Factor Libre, "
    "SDi Soluciones, "
    "PESOL ,"
    "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/helpdesk",
    "depends": ["project", "helpdesk_mgmt"],
    "data": [
        "views/helpdesk_project_task_views.xml",
        "views/helpdesk_project_ticket_views.xml",
    ],
    "demo": [],
    "development_status": "Alpha",
    "application": True,
    "installable": True,
}
