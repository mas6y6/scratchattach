"""
Enums stating the shape of a block from its opcode (i.e: stack, c-mouth, cap, hat etc)
"""
from __future__ import annotations

# Perhaps this should be merged with pallet.py
from dataclasses import dataclass
from typing import Final

from . import commons

from ..utils.enums import _EnumWrapper


class _Yesnt(commons.Singleton):
    """I can't really tell you if yesn't means yes or no; is it true or false? It depends."""
    def __bool__(self):
        raise TypeError("I can't really tell you if yesn't means yes or no; is it true or false? It depends.")


YESNT: Final[_Yesnt] = _Yesnt()
"""Value used when neither True nor False is applicable (when it depends on other factors)"""
print(id(YESNT.i_list))

@dataclass(init=True, repr=True)
class BlockShape:
    """
    A class that describes the shape of a block; e.g. is it a stack, c-mouth, cap, hat reporter, boolean or menu block?
    """
    is_stack: bool | _Yesnt = False  # Most blocks - e.g. move [10] steps
    is_c_mouth: bool | _Yesnt = False  # Has substack - e.g. repeat
    is_cap: bool | _Yesnt = False  # No next - e.g. forever
    is_hat: bool | _Yesnt = False  # No parent - e.g. when gf clicked
    is_reporter: bool | _Yesnt = False  # (reporter)
    is_boolean: bool | _Yesnt = False  # <reporter>
    is_menu: bool | _Yesnt = False  # Shadow reporters, e.g. costume menu
    opcode: str = None

    @property
    def is_attachable(self):
        if self.is_cap is YESNT:
            raise TypeError("Can't tell if the block is attachable because we can't be sure if it is a cap block or not (stop block)")
        return not self.is_cap and not self.is_reporter


class BlockShapes(_EnumWrapper):
    MOTION_MOVESTEPS = BlockShape(is_stack=True, opcode="motion_movesteps")
    MOTION_TURNRIGHT = BlockShape(is_stack=True, opcode="motion_turnright")
    MOTION_TURNLEFT = BlockShape(is_stack=True, opcode="motion_turnleft")
    MOTION_GOTO = BlockShape(is_stack=True, opcode="motion_goto")
    MOTION_GOTOXY = BlockShape(is_stack=True, opcode="motion_gotoxy")
    MOTION_GLIDETO = BlockShape(is_stack=True, opcode="motion_glideto")
    MOTION_GLIDESECSTOXY = BlockShape(is_stack=True, opcode="motion_glidesecstoxy")
    MOTION_POINTINDIRECTION = BlockShape(is_stack=True, opcode="motion_pointindirection")
    MOTION_POINTTOWARDS = BlockShape(is_stack=True, opcode="motion_pointtowards")
    MOTION_CHANGEXBY = BlockShape(is_stack=True, opcode="motion_changexby")
    MOTION_SETX = BlockShape(is_stack=True, opcode="motion_setx")
    MOTION_CHANGEYBY = BlockShape(is_stack=True, opcode="motion_changeyby")
    MOTION_SETY = BlockShape(is_stack=True, opcode="motion_sety")
    MOTION_IFONEDGEBOUNCE = BlockShape(is_stack=True, opcode="motion_ifonedgebounce")
    MOTION_SETROTATIONSTYLE = BlockShape(is_stack=True, opcode="motion_setrotationstyle")
    MOTION_XPOSITION = BlockShape(is_reporter=True, opcode="motion_xposition")
    MOTION_YPOSITION = BlockShape(is_reporter=True, opcode="motion_yposition")
    MOTION_DIRECTION = BlockShape(is_reporter=True, opcode="motion_direction")
    MOTION_SCROLL_RIGHT = BlockShape(is_stack=True, opcode="motion_scroll_right")
    MOTION_SCROLL_UP = BlockShape(is_stack=True, opcode="motion_scroll_up")
    MOTION_ALIGN_SCENE = BlockShape(is_stack=True, opcode="motion_align_scene")
    MOTION_XSCROLL = BlockShape(is_reporter=True, opcode="motion_xscroll")
    MOTION_YSCROLL = BlockShape(is_reporter=True, opcode="motion_yscroll")
    MOTION_GOTO_MENU = BlockShape(is_reporter=True, is_menu=True, opcode="motion_goto_menu")
    MOTION_GLIDETO_MENU = BlockShape(is_reporter=True, is_menu=True, opcode="motion_glideto_menu")
    MOTION_POINTTOWARDS_MENU = BlockShape(is_reporter=True, is_menu=True, opcode="motion_pointtowards_menu")

    LOOKS_SAYFORSECS = BlockShape(is_stack=True, opcode="looks_sayforsecs")
    LOOKS_SAY = BlockShape(is_stack=True, opcode="looks_say")
    LOOKS_THINKFORSECS = BlockShape(is_stack=True, opcode="looks_thinkforsecs")
    LOOKS_THINK = BlockShape(is_stack=True, opcode="looks_think")
    LOOKS_SWITCHCOSTUMETO = BlockShape(is_stack=True, opcode="looks_switchcostumeto")
    LOOKS_NEXTCOSTUME = BlockShape(is_stack=True, opcode="looks_nextcostume")
    LOOKS_SWITCHBACKDROPTO = BlockShape(is_stack=True, opcode="looks_switchbackdropto")
    LOOKS_SWITCHBACKDROPTOANDWAIT = BlockShape(is_stack=True, opcode="looks_switchbackdroptoandwait")
    LOOKS_NEXTBACKDROP = BlockShape(is_stack=True, opcode="looks_nextbackdrop")
    LOOKS_CHANGESIZEBY = BlockShape(is_stack=True, opcode="looks_changesizeby")
    LOOKS_SETSIZETO = BlockShape(is_stack=True, opcode="looks_setsizeto")
    LOOKS_CHANGEEFFECTBY = BlockShape(is_stack=True, opcode="looks_changeeffectby")
    LOOKS_SETEFFECTTO = BlockShape(is_stack=True, opcode="looks_seteffectto")
    LOOKS_CLEARGRAPHICEFFECTS = BlockShape(is_stack=True, opcode="looks_cleargraphiceffects")
    LOOKS_SHOW = BlockShape(is_stack=True, opcode="looks_show")
    LOOKS_HIDE = BlockShape(is_stack=True, opcode="looks_hide")
    LOOKS_GOTOFRONTBACK = BlockShape(is_stack=True, opcode="looks_gotofrontback")
    LOOKS_GOFORWARDBACKWARDLAYERS = BlockShape(is_stack=True, opcode="looks_goforwardbackwardlayers")
    LOOKS_COSTUMENUMBERNAME = BlockShape(is_reporter=True, opcode="looks_costumenumbername")
    LOOKS_BACKDROPNUMBERNAME = BlockShape(is_reporter=True, opcode="looks_backdropnumbername")
    LOOKS_SIZE = BlockShape(is_reporter=True, opcode="looks_size")
    LOOKS_HIDEALLSPRITES = BlockShape(is_stack=True, opcode="looks_hideallsprites")
    LOOKS_SETSTRETCHTO = BlockShape(is_stack=True, opcode="looks_setstretchto")
    LOOKS_CHANGESTRETCHBY = BlockShape(is_stack=True, opcode="looks_changestretchby")
    LOOKS_COSTUME = BlockShape(is_reporter=True, is_menu=True, opcode="looks_costume")
    LOOKS_BACKDROPS = BlockShape(is_reporter=True, is_menu=True, opcode="looks_backdrops")

    SOUND_PLAYUNTILDONE = BlockShape(is_stack=True, opcode="sound_playuntildone")
    SOUND_PLAY = BlockShape(is_stack=True, opcode="sound_play")
    SOUND_STOPALLSOUNDS = BlockShape(is_stack=True, opcode="sound_stopallsounds")
    SOUND_CHANGEEFFECTBY = BlockShape(is_stack=True, opcode="sound_changeeffectby")
    SOUND_SETEFFECTTO = BlockShape(is_stack=True, opcode="sound_seteffectto")
    SOUND_CLEAREFFECTS = BlockShape(is_stack=True, opcode="sound_cleareffects")
    SOUND_CHANGEVOLUMEBY = BlockShape(is_stack=True, opcode="sound_changevolumeby")
    SOUND_SETVOLUMETO = BlockShape(is_stack=True, opcode="sound_setvolumeto")
    SOUND_VOLUME = BlockShape(is_reporter=True, opcode="sound_volume")
    SOUND_SOUNDS_MENU = BlockShape(is_reporter=True, is_menu=True, opcode="sound_sounds_menu")

    EVENT_WHENFLAGCLICKED = BlockShape(is_hat=True, opcode="event_whenflagclicked")
    EVENT_WHENKEYPRESSED = BlockShape(is_hat=True, opcode="event_whenkeypressed")
    EVENT_WHENTHISSPRITECLICKED = BlockShape(is_hat=True, opcode="event_whenthisspriteclicked")
    EVENT_WHENSTAGECLICKED = BlockShape(is_hat=True, opcode="event_whenstageclicked")
    EVENT_WHENBACKDROPSWITCHESTO = BlockShape(is_hat=True, opcode="event_whenbackdropswitchesto")
    EVENT_WHENGREATERTHAN = BlockShape(is_hat=True, opcode="event_whengreaterthan")
    EVENT_WHENBROADCASTRECEIVED = BlockShape(is_hat=True, opcode="event_whenbroadcastreceived")
    EVENT_BROADCAST = BlockShape(is_stack=True, opcode="event_broadcast")
    EVENT_BROADCASTANDWAIT = BlockShape(is_stack=True, opcode="event_broadcastandwait")
    EVENT_WHENTOUCHINGOBJECT = BlockShape(is_hat=True, opcode="event_whentouchingobject")
    EVENT_BROADCAST_MENU = BlockShape(is_reporter=True, is_menu=True, opcode="event_broadcast_menu")
    EVENT_TOUCHINGOBJECTMENU = BlockShape(is_reporter=True, is_menu=True, opcode="event_touchingobjectmenu")

    CONTROL_WAIT = BlockShape(is_stack=True, opcode="control_wait")
    CONTROL_FOREVER = BlockShape(is_c_mouth=True, is_stack=True, is_cap=True, opcode="control_forever")
    CONTROL_IF = BlockShape(is_c_mouth=True, is_stack=True, opcode="control_if")
    CONTROL_IF_ELSE = BlockShape(is_c_mouth=True, is_stack=True, opcode="control_if_else")
    CONTROL_WAIT_UNTIL = BlockShape(is_stack=True, opcode="control_wait_until")
    CONTROL_REPEAT_UNTIL = BlockShape(is_c_mouth=True, is_stack=True, opcode="control_repeat_until")
    CONTROL_STOP = BlockShape(is_stack=True, is_cap=YESNT, opcode="control_stop")
    CONTROL_START_AS_CLONE = BlockShape(is_hat=True, opcode="control_start_as_clone")
    CONTROL_CREATE_CLONE_OF = BlockShape(is_stack=True, opcode="control_create_clone_of")
    CONTROL_DELETE_THIS_CLONE = BlockShape(is_stack=True, is_cap=True, opcode="control_delete_this_clone")
    CONTROL_FOR_EACH = BlockShape(is_c_mouth=True, is_stack=True, opcode="control_for_each")
    CONTROL_WHILE = BlockShape(is_c_mouth=True, is_stack=True, opcode="control_while")
    CONTROL_GET_COUNTER = BlockShape(is_reporter=True, opcode="control_get_counter")
    CONTROL_INCR_COUNTER = BlockShape(is_stack=True, opcode="control_incr_counter")
    CONTROL_CLEAR_COUNTER = BlockShape(is_stack=True, opcode="control_clear_counter")
    CONTROL_ALL_AT_ONCE = BlockShape(is_c_mouth=True, is_stack=True, opcode="control_all_at_once")
    CONTROL_CREATE_CLONE_OF_MENU = BlockShape(is_reporter=True, is_menu=True, opcode="control_create_clone_of_menu")

    SENSING_TOUCHINGOBJECT = BlockShape(is_reporter=True, is_boolean=True, opcode="sensing_touchingobject")
    SENSING_TOUCHINGCOLOR = BlockShape(is_reporter=True, is_boolean=True, opcode="sensing_touchingcolor")
    SENSING_COLORISTOUCHINGCOLOR = BlockShape(is_reporter=True, is_boolean=True, opcode="sensing_coloristouchingcolor")
    SENSING_DISTANCETO = BlockShape(is_reporter=True, opcode="sensing_distanceto")
    SENSING_ASKANDWAIT = BlockShape(is_stack=True, opcode="sensing_askandwait")
    SENSING_ANSWER = BlockShape(is_reporter=True, opcode="sensing_answer")
    SENSING_KEYPRESSED = BlockShape(is_reporter=True, is_boolean=True, opcode="sensing_keypressed")
    SENSING_MOUSEDOWN = BlockShape(is_reporter=True, is_boolean=True, opcode="sensing_mousedown")
    SENSING_MOUSEX = BlockShape(is_reporter=True, opcode="sensing_mousex")
    SENSING_MOUSEY = BlockShape(is_reporter=True, opcode="sensing_mousey")
    SENSING_SETDRAGMODE = BlockShape(is_stack=True, opcode="sensing_setdragmode")
    SENSING_LOUDNESS = BlockShape(is_reporter=True, opcode="sensing_loudness")
    SENSING_TIMER = BlockShape(is_reporter=True, opcode="sensing_timer")
    SENSING_RESETTIMER = BlockShape(is_stack=True, opcode="sensing_resettimer")
    SENSING_OF = BlockShape(is_reporter=True, opcode="sensing_of")
    SENSING_CURRENT = BlockShape(is_reporter=True, opcode="sensing_current")
    SENSING_DAYSSINCE2000 = BlockShape(is_reporter=True, opcode="sensing_dayssince2000")
    SENSING_USERNAME = BlockShape(is_reporter=True, opcode="sensing_username")
    SENSING_LOUD = BlockShape(is_reporter=True, is_boolean=True, opcode="sensing_loud")
    SENSING_USERID = BlockShape(is_reporter=True, opcode="sensing_userid")
    SENSING_TOUCHINGOBJECTMENU = BlockShape(is_reporter=True, is_menu=True, opcode="sensing_touchingobjectmenu")
    SENSING_DISTANCETOMENU = BlockShape(is_reporter=True, is_menu=True, opcode="sensing_distancetomenu")
    SENSING_KEYOPTIONS = BlockShape(is_reporter=True, is_menu=True, opcode="sensing_keyoptions")
    SENSING_OF_OBJECT_MENU = BlockShape(is_reporter=True, is_menu=True, opcode="sensing_of_object_menu")

    OPERATOR_ADD = BlockShape(is_reporter=True, opcode="operator_add")
    OPERATOR_SUBTRACT = BlockShape(is_reporter=True, opcode="operator_subtract")
    OPERATOR_MULTIPLY = BlockShape(is_reporter=True, opcode="operator_multiply")
    OPERATOR_DIVIDE = BlockShape(is_reporter=True, opcode="operator_divide")
    OPERATOR_RANDOM = BlockShape(is_reporter=True, opcode="operator_random")
    OPERATOR_GT = BlockShape(is_reporter=True, is_boolean=True, opcode="operator_gt")
    OPERATOR_LT = BlockShape(is_reporter=True, is_boolean=True, opcode="operator_lt")
    OPERATOR_EQUALS = BlockShape(is_reporter=True, is_boolean=True, opcode="operator_equals")
    OPERATOR_AND = BlockShape(is_reporter=True, is_boolean=True, opcode="operator_and")
    OPERATOR_OR = BlockShape(is_reporter=True, is_boolean=True, opcode="operator_or")
    OPERATOR_NOT = BlockShape(is_reporter=True, is_boolean=True, opcode="operator_not")
    OPERATOR_JOIN = BlockShape(is_reporter=True, opcode="operator_join")
    OPERATOR_LETTER_OF = BlockShape(is_reporter=True, opcode="operator_letter_of")
    OPERATOR_LENGTH = BlockShape(is_reporter=True, opcode="operator_length")
    OPERATOR_CONTAINS = BlockShape(is_reporter=True, is_boolean=True, opcode="operator_contains")
    OPERATOR_MOD = BlockShape(is_reporter=True, opcode="operator_mod")
    OPERATOR_ROUND = BlockShape(is_reporter=True, opcode="operator_round")
    OPERATOR_MATHOP = BlockShape(is_reporter=True, opcode="operator_mathop")

    DATA_VARIABLE = BlockShape(is_reporter=True, opcode="data_variable")
    DATA_SETVARIABLETO = BlockShape(is_stack=True, opcode="data_setvariableto")
    DATA_CHANGEVARIABLEBY = BlockShape(is_stack=True, opcode="data_changevariableby")
    DATA_SHOWVARIABLE = BlockShape(is_stack=True, opcode="data_showvariable")
    DATA_HIDEVARIABLE = BlockShape(is_stack=True, opcode="data_hidevariable")
    DATA_LISTCONTENTS = BlockShape(is_reporter=True, opcode="data_listcontents")
    DATA_ADDTOLIST = BlockShape(is_stack=True, opcode="data_addtolist")
    DATA_DELETEOFLIST = BlockShape(is_stack=True, opcode="data_deleteoflist")
    DATA_DELETEALLOFLIST = BlockShape(is_stack=True, opcode="data_deletealloflist")
    DATA_INSERTATLIST = BlockShape(is_stack=True, opcode="data_insertatlist")
    DATA_REPLACEITEMOFLIST = BlockShape(is_stack=True, opcode="data_replaceitemoflist")
    DATA_ITEMOFLIST = BlockShape(is_reporter=True, is_boolean=True, opcode="data_itemoflist")
    DATA_ITEMNUMOFLIST = BlockShape(is_reporter=True, opcode="data_itemnumoflist")
    DATA_LENGTHOFLIST = BlockShape(is_reporter=True, opcode="data_lengthoflist")
    DATA_LISTCONTAINSITEM = BlockShape(is_reporter=True, is_boolean=True, opcode="data_listcontainsitem")
    DATA_SHOWLIST = BlockShape(is_stack=True, opcode="data_showlist")
    DATA_HIDELIST = BlockShape(is_stack=True, opcode="data_hidelist")
    DATA_LISTINDEXALL = BlockShape(is_reporter=True, is_menu=True, opcode="data_listindexall")
    DATA_LISTINDEXRANDOM = BlockShape(is_reporter=True, is_menu=True, opcode="data_listindexrandom")

    PROCEDURES_DEFINITION = BlockShape(is_hat=True, opcode="procedures_definition")
    PROCEDURES_CALL = BlockShape(is_stack=True, opcode="procedures_call")
    PROCEDURES_DECLARATION = BlockShape(is_stack=True, opcode="procedures_declaration")
    PROCEDURES_PROTOTYPE = BlockShape(is_stack=True, opcode="procedures_prototype")

    ARGUMENT_REPORTER_STRING_NUMBER = BlockShape(is_reporter=True, opcode="argument_reporter_string_number")
    ARGUMENT_REPORTER_BOOLEAN = BlockShape(is_reporter=True, is_boolean=True, opcode="argument_reporter_boolean")
    ARGUMENT_EDITOR_REPORTER = BlockShape(is_reporter=True, is_boolean=True, opcode="argument_editor_reporter")
    ARGUMENT_EDITOR_STRING_NUMBER = BlockShape(is_reporter=True, opcode="argument_editor_string_number")

    MUSIC_PLAYDRUMFORBEATS = BlockShape(is_stack=True, opcode="music_playDrumForBeats")
    MUSIC_RESTFORBEATS = BlockShape(is_stack=True, opcode="music_restForBeats")
    MUSIC_PLAYNOTEFORBEATS = BlockShape(is_stack=True, opcode="music_playNoteForBeats")
    MUSIC_SETINSTRUMENT = BlockShape(is_stack=True, opcode="music_setInstrument")
    MUSIC_SETTEMPO = BlockShape(is_stack=True, opcode="music_setTempo")
    MUSIC_CHANGETEMPO = BlockShape(is_stack=True, opcode="music_changeTempo")
    MUSIC_GETTEMPO = BlockShape(is_reporter=True, opcode="music_getTempo")
    MUSIC_MIDIPLAYDRUMFORBEATS = BlockShape(is_stack=True, opcode="music_midiPlayDrumForBeats")
    MUSIC_MIDISETINSTRUMENT = BlockShape(is_stack=True, opcode="music_midiSetInstrument")
    MUSIC_MENU_DRUM = BlockShape(is_reporter=True, is_menu=True, opcode="music_menu_DRUM")
    MUSIC_MENU_INSTRUMENT = BlockShape(is_reporter=True, is_menu=True, opcode="music_menu_INSTRUMENT")

    PEN_CLEAR = BlockShape(is_stack=True, opcode="pen_clear")
    PEN_STAMP = BlockShape(is_stack=True, opcode="pen_stamp")
    PEN_PENDOWN = BlockShape(is_stack=True, opcode="pen_penDown")
    PEN_PENUP = BlockShape(is_stack=True, opcode="pen_penUp")
    PEN_SETPENCOLORTOCOLOR = BlockShape(is_stack=True, opcode="pen_setPenColorToColor")
    PEN_CHANGEPENCOLORPARAMBY = BlockShape(is_stack=True, opcode="pen_changePenColorParamBy")
    PEN_SETPENCOLORPARAMTO = BlockShape(is_stack=True, opcode="pen_setPenColorParamTo")
    PEN_CHANGEPENSIZEBY = BlockShape(is_stack=True, opcode="pen_changePenSizeBy")
    PEN_SETPENSIZETO = BlockShape(is_stack=True, opcode="pen_setPenSizeTo")
    PEN_SETPENHUETONUMBER = BlockShape(is_stack=True, opcode="pen_setPenHueToNumber")
    PEN_CHANGEPENHUEBY = BlockShape(is_stack=True, opcode="pen_changePenHueBy")
    PEN_SETPENSHADETONUMBER = BlockShape(is_stack=True, opcode="pen_setPenShadeToNumber")
    PEN_CHANGEPENSHADEBY = BlockShape(is_stack=True, opcode="pen_changePenShadeBy")
    PEN_MENU_COLORPARAM = BlockShape(is_reporter=True, is_menu=True, opcode="pen_menu_colorParam")

    VIDEOSENSING_WHENMOTIONGREATERTHAN = BlockShape(is_hat=True, opcode="videoSensing_whenMotionGreaterThan")
    VIDEOSENSING_VIDEOON = BlockShape(is_reporter=True, opcode="videoSensing_videoOn")
    VIDEOSENSING_VIDEOTOGGLE = BlockShape(is_stack=True, opcode="videoSensing_videoToggle")
    VIDEOSENSING_SETVIDEOTRANSPARENCY = BlockShape(is_stack=True, opcode="videoSensing_setVideoTransparency")
    VIDEOSENSING_MENU_ATTRIBUTE = BlockShape(is_reporter=True, is_menu=True, opcode="videoSensing_menu_ATTRIBUTE")
    VIDEOSENSING_MENU_SUBJECT = BlockShape(is_reporter=True, is_menu=True, opcode="videoSensing_menu_SUBJECT")
    VIDEOSENSING_MENU_VIDEO_STATE = BlockShape(is_reporter=True, is_menu=True, opcode="videoSensing_menu_VIDEO_STATE")

    TEXT2SPEECH_SPEAKANDWAIT = BlockShape(is_stack=True, opcode="text2speech_speakAndWait")
    TEXT2SPEECH_SETVOICE = BlockShape(is_stack=True, opcode="text2speech_setVoice")
    TEXT2SPEECH_SETLANGUAGE = BlockShape(is_stack=True, opcode="text2speech_setLanguage")
    TEXT2SPEECH_MENU_VOICES = BlockShape(is_reporter=True, is_menu=True, opcode="text2speech_menu_voices")
    TEXT2SPEECH_MENU_LANGUAGES = BlockShape(is_reporter=True, is_menu=True, opcode="text2speech_menu_languages")
    TRANSLATE_GETTRANSLATE = BlockShape(is_reporter=True, opcode="translate_getTranslate")
    TRANSLATE_GETVIEWERLANGUAGE = BlockShape(is_reporter=True, opcode="translate_getViewerLanguage")
    TRANSLATE_MENU_LANGUAGES = BlockShape(is_reporter=True, is_menu=True, opcode="translate_menu_languages")

    MAKEYMAKEY_WHENMAKEYKEYPRESSED = BlockShape(is_hat=True, opcode="makeymakey_whenMakeyKeyPressed")
    MAKEYMAKEY_WHENCODEPRESSED = BlockShape(is_hat=True, opcode="makeymakey_whenCodePressed")
    MAKEYMAKEY_MENU_KEY = BlockShape(is_reporter=True, is_menu=True, opcode="makeymakey_menu_KEY")
    MAKEYMAKEY_MENU_SEQUENCE = BlockShape(is_reporter=True, is_menu=True, opcode="makeymakey_menu_SEQUENCE")

    MICROBIT_WHENBUTTONPRESSED = BlockShape(opcode="microbit_whenButtonPressed")
    MICROBIT_ISBUTTONPRESSED = BlockShape(opcode="microbit_isButtonPressed")
    MICROBIT_WHENGESTURE = BlockShape(opcode="microbit_whenGesture")
    MICROBIT_DISPLAYSYMBOL = BlockShape(opcode="microbit_displaySymbol")
    MICROBIT_DISPLAYTEXT = BlockShape(opcode="microbit_displayText")
    MICROBIT_DISPLAYCLEAR = BlockShape(opcode="microbit_displayClear")
    MICROBIT_WHENTILTED = BlockShape(opcode="microbit_whenTilted")
    MICROBIT_ISTILTED = BlockShape(opcode="microbit_isTilted")
    MICROBIT_GETTILTANGLE = BlockShape(opcode="microbit_getTiltAngle")
    MICROBIT_WHENPINCONNECTED = BlockShape(opcode="microbit_whenPinConnected")
    MICROBIT_MENU_BUTTONS = BlockShape(opcode="microbit_menu_buttons")
    MICROBIT_MENU_GESTURES = BlockShape(opcode="microbit_menu_gestures")
    MICROBIT_MENU_TILTDIRECTIONANY = BlockShape(opcode="microbit_menu_tiltDirectionAny")
    MICROBIT_MENU_TILTDIRECTION = BlockShape(opcode="microbit_menu_tiltDirection")
    MICROBIT_MENU_TOUCHPINS = BlockShape(opcode="microbit_menu_touchPins")
    MICROBIT_MENU_PINSTATE = BlockShape(opcode="microbit_menu_pinState")

    EV3_MOTORTURNCLOCKWISE = BlockShape(opcode="ev3_motorTurnClockwise")
    EV3_MOTORTURNCOUNTERCLOCKWISE = BlockShape(opcode="ev3_motorTurnCounterClockwise")
    EV3_MOTORSETPOWER = BlockShape(opcode="ev3_motorSetPower")
    EV3_GETMOTORPOSITION = BlockShape(opcode="ev3_getMotorPosition")
    EV3_WHENBUTTONPRESSED = BlockShape(opcode="ev3_whenButtonPressed")
    EV3_WHENDISTANCELESSTHAN = BlockShape(opcode="ev3_whenDistanceLessThan")
    EV3_WHENBRIGHTNESSLESSTHAN = BlockShape(opcode="ev3_whenBrightnessLessThan")
    EV3_BUTTONPRESSED = BlockShape(opcode="ev3_buttonPressed")
    EV3_GETDISTANCE = BlockShape(opcode="ev3_getDistance")
    EV3_GETBRIGHTNESS = BlockShape(opcode="ev3_getBrightness")
    EV3_BEEP = BlockShape(opcode="ev3_beep")
    EV3_MENU_MOTORPORTS = BlockShape(opcode="ev3_menu_motorPorts")
    EV3_MENU_SENSORPORTS = BlockShape(opcode="ev3_menu_sensorPorts")

    BOOST_MOTORONFOR = BlockShape(opcode="boost_motorOnFor")
    BOOST_MOTORONFORROTATION = BlockShape(opcode="boost_motorOnForRotation")
    BOOST_MOTORON = BlockShape(opcode="boost_motorOn")
    BOOST_MOTOROFF = BlockShape(opcode="boost_motorOff")
    BOOST_SETMOTORPOWER = BlockShape(opcode="boost_setMotorPower")
    BOOST_SETMOTORDIRECTION = BlockShape(opcode="boost_setMotorDirection")
    BOOST_GETMOTORPOSITION = BlockShape(opcode="boost_getMotorPosition")
    BOOST_WHENCOLOR = BlockShape(opcode="boost_whenColor")
    BOOST_SEEINGCOLOR = BlockShape(opcode="boost_seeingColor")
    BOOST_WHENTILTED = BlockShape(opcode="boost_whenTilted")
    BOOST_GETTILTANGLE = BlockShape(opcode="boost_getTiltAngle")
    BOOST_SETLIGHTHUE = BlockShape(opcode="boost_setLightHue")
    BOOST_MENU_MOTOR_ID = BlockShape(opcode="boost_menu_MOTOR_ID")
    BOOST_MENU_MOTOR_DIRECTION = BlockShape(opcode="boost_menu_MOTOR_DIRECTION")
    BOOST_MENU_MOTOR_REPORTER_ID = BlockShape(opcode="boost_menu_MOTOR_REPORTER_ID")
    BOOST_MENU_COLOR = BlockShape(opcode="boost_menu_COLOR")
    BOOST_MENU_TILT_DIRECTION_ANY = BlockShape(opcode="boost_menu_TILT_DIRECTION_ANY")
    BOOST_MENU_TILT_DIRECTION = BlockShape(opcode="boost_menu_TILT_DIRECTION")

    WEDO2_MOTORONFOR = BlockShape(opcode="wedo2_motorOnFor")
    WEDO2_MOTORON = BlockShape(opcode="wedo2_motorOn")
    WEDO2_MOTOROFF = BlockShape(opcode="wedo2_motorOff")
    WEDO2_STARTMOTORPOWER = BlockShape(opcode="wedo2_startMotorPower")
    WEDO2_SETMOTORDIRECTION = BlockShape(opcode="wedo2_setMotorDirection")
    WEDO2_SETLIGHTHUE = BlockShape(opcode="wedo2_setLightHue")
    WEDO2_WHENDISTANCE = BlockShape(opcode="wedo2_whenDistance")
    WEDO2_WHENTILTED = BlockShape(opcode="wedo2_whenTilted")
    WEDO2_GETDISTANCE = BlockShape(opcode="wedo2_getDistance")
    WEDO2_ISTILTED = BlockShape(opcode="wedo2_isTilted")
    WEDO2_GETTILTANGLE = BlockShape(opcode="wedo2_getTiltAngle")
    WEDO2_PLAYNOTEFOR = BlockShape(opcode="wedo2_playNoteFor")
    WEDO2_MENU_MOTOR_ID = BlockShape(opcode="wedo2_menu_MOTOR_ID")
    WEDO2_MENU_MOTOR_DIRECTION = BlockShape(opcode="wedo2_menu_MOTOR_DIRECTION")
    WEDO2_MENU_OP = BlockShape(opcode="wedo2_menu_OP")
    WEDO2_MENU_TILT_DIRECTION_ANY = BlockShape(opcode="wedo2_menu_TILT_DIRECTION_ANY")
    WEDO2_MENU_TILT_DIRECTION = BlockShape(opcode="wedo2_menu_TILT_DIRECTION")

    GDXFOR_WHENGESTURE = BlockShape(opcode="gdxfor_whenGesture")
    GDXFOR_WHENFORCEPUSHEDORPULLED = BlockShape(opcode="gdxfor_whenForcePushedOrPulled")
    GDXFOR_GETFORCE = BlockShape(opcode="gdxfor_getForce")
    GDXFOR_WHENTILTED = BlockShape(opcode="gdxfor_whenTilted")
    GDXFOR_ISTILTED = BlockShape(opcode="gdxfor_isTilted")
    GDXFOR_GETTILT = BlockShape(opcode="gdxfor_getTilt")
    GDXFOR_ISFREEFALLING = BlockShape(opcode="gdxfor_isFreeFalling")
    GDXFOR_GETSPINSPEED = BlockShape(opcode="gdxfor_getSpinSpeed")
    GDXFOR_GETACCELERATION = BlockShape(opcode="gdxfor_getAcceleration")
    GDXFOR_MENU_GESTUREOPTIONS = BlockShape(opcode="gdxfor_menu_gestureOptions")
    GDXFOR_MENU_PUSHPULLOPTIONS = BlockShape(opcode="gdxfor_menu_pushPullOptions")
    GDXFOR_MENU_TILTANYOPTIONS = BlockShape(opcode="gdxfor_menu_tiltAnyOptions")
    GDXFOR_MENU_TILTOPTIONS = BlockShape(opcode="gdxfor_menu_tiltOptions")
    GDXFOR_MENU_AXISOPTIONS = BlockShape(opcode="gdxfor_menu_axisOptions")

    COREEXAMPLE_EXAMPLEOPCODE = BlockShape(is_reporter=True, opcode="coreExample_exampleOpcode")
    COREEXAMPLE_EXAMPLEWITHINLINEIMAGE = BlockShape(is_stack=True, opcode="coreExample_exampleWithInlineImage")

    NOTE = BlockShape(is_reporter=True, is_menu=True, opcode="note")
    MATRIX = BlockShape(is_reporter=True, is_menu=True, opcode="matrix")
    UNDEFINED = BlockShape(is_hat=True, is_cap=True, opcode="red_hat_block")
