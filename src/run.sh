Run() {
	THIS_DIR="$(cd $(dirname $0); pwd)"
	echo -e "A\n\tB" | "${THIS_DIR}/StdIn.py"
# 永久待機……
#	"${THIS_DIR}/StdIn.py"

# 永久待機……
#	"${THIS_DIR}/client.py"
	"${THIS_DIR}/client_O_NONBLOCK.py"
	"${THIS_DIR}/client_thread.py"
# stdin無視……
	echo -e "A\n\tB" | "${THIS_DIR}/client_O_NONBLOCK.py"
	echo -e "A\n\tB" | "${THIS_DIR}/client_thread.py"
}
Run "$@"
