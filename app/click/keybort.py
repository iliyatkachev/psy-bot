from aiogram.types import InlineKeyboardButton

button = [
    [
        InlineKeyboardButton(text="обращение📖", callback_data="get"),
        InlineKeyboardButton(text="Служба Поддержки🥸", url="https://t.me/Iltk01")
    ]
]


admin_button = [
    [
        InlineKeyboardButton(text="Статистика🪪", callback_data="a_stat"),
        InlineKeyboardButton(text="Каналы", callback_data="channels")

    ],
    [
        InlineKeyboardButton(text="Добавить пост", callback_data="mailing"),
        InlineKeyboardButton(text="Управление администраторами", callback_data="admin_opportunities")
    ],
    [
        InlineKeyboardButton(text="Вернуться в меню🔙", callback_data="button_users")
    ]
]


admin_menu_button = [
    [
        InlineKeyboardButton(text='Вернуться в админ меню🔙', callback_data="back_a_m")
    ]
]


a_stat_button = [
    [
        InlineKeyboardButton(text="Отображение пользователей🪬", callback_data="s_full_users")
    ],
       [
        InlineKeyboardButton(text="Вернуться в меню🔙", callback_data="back_a_m")
    ]
]


a_channels_button = [
    [
        InlineKeyboardButton(text="Добавить✔️", callback_data="a_c_add"),
        InlineKeyboardButton(text="удалить❌", callback_data="a_c_delete")
    ],
    [
        InlineKeyboardButton(text='Вернуться в админ меню🔙', callback_data="back_a_m")
    ]
]


a_mailing_button = [
    [
        InlineKeyboardButton(text="Добавить✔️", callback_data="a_m_add"),
        InlineKeyboardButton(text="Вернуться в меню🔙", callback_data="back_a_m")
    ]
]


a_opportunities_button = [
    [
        InlineKeyboardButton(text="Список админов", callback_data="list_admin"),

    ],
    [
        InlineKeyboardButton(text="Добавить админа", callback_data="add_admin"),
        InlineKeyboardButton(text="удалить админа", callback_data="delete_admin")
    ],
    [
        InlineKeyboardButton(text="Вернуться в меню🔙", callback_data="back_a_m")
    ]
]