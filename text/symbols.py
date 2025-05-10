""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''
_pad        = '_'
_punctuation = ';:,.!?¡¿—…"«»“” '
# _letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# _letters_ipa = "ɑɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘'̩'ᵻ"
_letters = ['$', '$$', '*', '**', '<', 'A', 'AA', 'D', 'DD', 'E', 'EE', 'H', 'HH', 'I0', 'I1', 'II0', 'S', 'SS', 'T', 'TT', 'U0', 'U1', 'UU0', 'Z', 'ZZ', '^', '^^', 'a', 'aa', 'b', 'bb', 'd', 'dd', 'f', 'ff', 'g', 'gg', 'h', 'hh', 'i0', 'i1', 'ii0', 'j', 'jj', 'k', 'kk', 'l', 'll', 'm', 'mm', 'n', 'nn', 'q', 'qq', 'r', 'rr', 's', 'ss', 't', 'tt', 'u0', 'u1', 'uu0', 'w', 'ww', 'x', 'xx', 'y', 'yy', 'z', 'zz']


# Export all symbols:
# symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)
symbols = [_pad] + list(_letters) + [" "]

# Special symbol ids
SPACE_ID = symbols.index(" ")
