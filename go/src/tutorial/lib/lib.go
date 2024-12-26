package lib

func IsDigit(s int32) bool {
	return '0' <= s && s <= '9'
}

func isSpace(s int32) bool {
	switch s {
	case ' ', '\t', '\n', '\r', '\v', '\f', 0x85, 0xA0:
		return true
	default:
		return false
	}
}
