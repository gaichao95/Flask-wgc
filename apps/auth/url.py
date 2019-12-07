from .register import RegisterHandler
from .index import IndexHandler
from .login import LoginHandler
from .logout import LogoutHandler
from .flow import FlowHandler
from .port import PortHandler

urls = [
    ("/", IndexHandler.as_view("user")),
    ("/auth/login", LoginHandler.as_view("user_login")),
    ("/auth/register", RegisterHandler.as_view("user_register")),
    ("/auth/logout", LogoutHandler.as_view("user_logout")),
    ("/auth/flow", FlowHandler.as_view("flow")),
    ("/auth/port", PortHandler.as_view("port"))
]
