import sys
from pathlib import Path

# Добавляем корневую директорию проекта в PYTHONPATH
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Импортируем фикстуры после добавления пути
from fixtures.browsers import (
    chromium_page,
    chromium_page_with_state,
    initialize_browser_state,
)
from fixtures.pages import (
    login_page,
    registration_page,
    dashboard_page,
    dashboard_page_with_state,
    courses_list_page,
    create_course_page,
)
