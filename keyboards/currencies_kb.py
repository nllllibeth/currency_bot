from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_currencies = InlineKeyboardMarkup(inline_keyboard=[
    [
    InlineKeyboardButton(
    text = 'Bitcoin',
    callback_data='currency_BTC'
    ),
    InlineKeyboardButton(
    text = 'Ethereum',
    callback_data='currency_ETH'
    ),
    ],
    [
    InlineKeyboardButton(
    text = 'BNB',
    callback_data='currency_BNB'
    ),
    InlineKeyboardButton(
    text = 'XRP',
    callback_data='currency_XRP'
    ),
    ],
    [
    InlineKeyboardButton(
    text = 'Cardano',
    callback_data='currency_ADA'
    ),
    InlineKeyboardButton(
    text = 'Binance USD',
    callback_data='currency_BUSD'
    ),
    ],
    [
    InlineKeyboardButton(
    text = 'Polygon',
    callback_data='currency_MATIC'
    ),
    InlineKeyboardButton(
    text = 'Dodgecoin',
    callback_data='currency_DOGE'
    ),
    ],
    [
    InlineKeyboardButton(
    text = 'Solana',
    callback_data='currency_SOL'
    ),
    InlineKeyboardButton(
    text = 'Polkadot',
    callback_data='currency_DOT'
    ),
    ],
    [
    InlineKeyboardButton(
    text = 'SHIBA INU',
    callback_data='currency_SHIB'
    ),
    InlineKeyboardButton(
    text = 'Litecoin',
    callback_data='currency_LTC'
    ),
    ]
])