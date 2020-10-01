from state import getOrCreateUser, createTransaction
import random
from args import parseArgs, ARG_INT


def get_amount_helper(msg, name) -> int:
	args = parseArgs(msg, [ARG_INT], [False], "/{} [amount]".format(name))
	if isinstance(args[0], int):
		if args[0] <= 0:
			msg.reply_text("Amount must be a positive integer")
			return 0
		elif args[0] > 10:
			msg.reply_text("Amount max. is 10!")
			return 0
		return args[0]
	elif not args[0]:
		return 1
	else:
		msg.reply_text("Unknown parsing error")
		return 0


def drink(bot, update):
	num = get_amount_helper(update.message, "drink")
	if num > 0:
		user = getOrCreateUser(update.message.from_user)
		createTransaction(user, -100 * num, "drink x{}".format(num))
		update.message.reply_text("OK, enjoy your {}!".format('🍹'*num), disable_notification=True)


hydrationMessages = [
	("OK, enjoy your {}!", "🍼"),
	("HYDRATION! {}", "💦"),
	("Hydrier dich! {}", "💦"),
	("Hydrieren sie sich bitte! {}", "💦"),
	("Der Bahnbabo sagt: Hydriert euch! {}", "💪")
]


def water(bot, update):
	num = get_amount_helper(update.message, "water")
	if num > 0:
		user = getOrCreateUser(update.message.from_user)
		createTransaction(user, -50 * num, "water x{}".format(num))
		answer = random.choice(hydrationMessages)
		update.message.reply_text(answer[0].format(answer[1]*num), disable_notification=True)


def pizza(bot, update):
	num = get_amount_helper(update.message, "pizza")
	if num > 0:
		user = getOrCreateUser(update.message.from_user)
		createTransaction(user, -200 * num, "pizza x{}".format(num))
		update.message.reply_text("Buon appetito! {}".format('🍕'*num), disable_notification=True)


def ice(bot, update):
	num = get_amount_helper(update.message, "ice")
	if num > 0:
		user = getOrCreateUser(update.message.from_user)
		createTransaction(user, -50 * num, "ice x{}".format(num))
		update.message.reply_text("Have a sweet one! {}".format('🚅'*num), disable_notification=True)
