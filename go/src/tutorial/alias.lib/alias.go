package alias

func IsDigit2(s int32) bool {
	return '0' <= s && s <= '9'
}

func isSpace2(s int32) bool {
	switch s {
	case ' ', '\t', '\n', '\r', '\v', '\f', 0x85, 0xA0:
		return true
	default:
		return false
	}
}
