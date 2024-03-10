from conversations.profile.buttons import HIDE_SEARCH_BUTTON, SHOW_SEARCH_BUTTON

MIN_AGE = 18
MAX_AGE = 99
MIN_NAME_LENGTH = 3
MAX_NAME_LENGTH = 30
MIN_ABOUT_LENGTH = 0
MAX_ABOUT_LENGTH = 1000
NAME_PATTERN = "^[А-Яа-яA-Za-z'-]+$"
AGE_PATTERN = "^([0-9]{3})$"

AGE_FIELD = "age"
SEX_FIELD = "sex"
NAME_FIELD = "name"
LOCATION_FIELD = "location"
ABOUT_FIELD = "about"
IMAGE_FIELD = "image"
IS_VISIBLE_FIELD = "is_visible"
RECEIVED_PHOTOS_FIELD = "received_photos"

ASK_AGE = "Хорошо. Давай познакомимся. Сколько тебе лет?"
ASK_SEX = "Ты парень или девушка?"
ASK_NAME = "Укажи свое имя:"
ASK_LOCATION = "В каком городе ты ищешь коливинг?"
ASK_ABOUT = "Расскажи о себе. Чем интересуешься, чем занимаешься?"
ASK_PHOTO = "Отправь фотографии, а затем нажми на кнопку, чтобы их сохранить."
DONT_SAVE_WITHOUT_PHOTO = "Нельзя сохранить анкету без фото."
LOOK_AT_FORM_FIRST = (
    "О, классная фотка. Давай взглянем на то, как выглядит твоя анкета:"
)
LOOK_AT_FORM_SECOND = "Супер. Теперь твоя анкета выглядит так."
LOOK_AT_FORM_THIRD = "Мне нравится! Давай взглянем на то, как выглядит твоя анкета:"
ASK_IS_THAT_RIGHT = "Всё верно?"
ASK_FORM_VISIBLE = "Сейчас твоя анкета видна всем, хочешь скрыть её?"
FORM_SAVED = "Анкета успешно сохранена."
FORM_EDIT_SAVED = "Отлично! Изменения сохранены."
FORM_NOT_CHANGED = "Хорошо. Анкета не изменилась."
FORM_IS_VISIBLE = (
    f"<b>Твой ответ:</b> {SHOW_SEARCH_BUTTON}\nТеперь твоя анкета видна в поиске."
)
FORM_IS_NOT_VISIBLE = (
    f"<b>Твой ответ:</b> {HIDE_SEARCH_BUTTON}\nТеперь твоя анкета не видна в поиске."
)
ASK_WANT_TO_CHANGE = "Что ты хочешь изменить?"
ASK_AGE_AGAIN = "Сколько тебе лет?"
ASK_NEW_PHOTO = "Отправь новые фотографии, а затем нажми на кнопку, чтобы их сохранить."
# fmt: off
AGE_ERROR_MSG = (
    'Введи целое число от {min} до {max}:'
)
NAME_LENGHT_ERROR_MSG = (
    'Введи имя от {min} до {max} символов:'
)
# fmt: on
DEFAULT_ERROR_MESSAGE = "Некорректный ввод."
NAME_SYMBOL_ERROR_MSG = "Введи имя без цифр и спецсимволов:"
BUTTON_ERROR_MSG = "Выбери соответствующий вариант:"
ABOUT_MAX_LEN_ERROR_MSG = (
    "Описание не должно содержать более {max} символов. Попробуй еще раз:"
)
PHOTO_ERROR_MESSAGE = "Отправь фото."
PROFILE_DATA = (
    "<b>Имя:</b> {name}\n"
    "<b>Пол:</b> {sex}\n"
    "<b>Возраст:</b> {age}\n"
    "<b>Место проживания:</b> {location}\n"
    "<b>О себе:</b> {about}\n"
    "<b>Видимость анкеты:</b> {is_visible}\n"
)
PROFILE_IS_VISIBLE_TEXT = "Отображается в поиске"
PROFILE_IS_INVISIBLE_TEXT = "Скрыта из поиска"
