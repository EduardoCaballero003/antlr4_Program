# Generated from grammarTraductor.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,115,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,3,2,40,8,
        2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,3,3,49,8,3,1,4,1,4,1,4,5,4,54,8,4,
        10,4,12,4,57,9,4,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,9,
        1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,81,8,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,95,8,
        10,10,10,12,10,98,9,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,12,3,12,110,8,12,1,12,1,12,1,12,1,12,0,1,20,13,0,2,4,6,8,10,
        12,14,16,18,20,22,24,0,0,114,0,27,1,0,0,0,2,33,1,0,0,0,4,35,1,0,
        0,0,6,48,1,0,0,0,8,50,1,0,0,0,10,58,1,0,0,0,12,60,1,0,0,0,14,64,
        1,0,0,0,16,66,1,0,0,0,18,69,1,0,0,0,20,80,1,0,0,0,22,99,1,0,0,0,
        24,104,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,
        0,0,0,29,30,1,0,0,0,30,1,1,0,0,0,31,34,3,4,2,0,32,34,3,24,12,0,33,
        31,1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,0,35,36,5,1,0,0,36,37,5,4,0,
        0,37,39,5,5,0,0,38,40,3,8,4,0,39,38,1,0,0,0,39,40,1,0,0,0,40,41,
        1,0,0,0,41,42,5,6,0,0,42,43,5,8,0,0,43,44,3,6,3,0,44,5,1,0,0,0,45,
        49,3,16,8,0,46,49,3,18,9,0,47,49,3,22,11,0,48,45,1,0,0,0,48,46,1,
        0,0,0,48,47,1,0,0,0,49,7,1,0,0,0,50,55,3,10,5,0,51,52,5,7,0,0,52,
        54,3,10,5,0,53,51,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,
        0,0,56,9,1,0,0,0,57,55,1,0,0,0,58,59,5,4,0,0,59,11,1,0,0,0,60,61,
        3,14,7,0,61,62,5,7,0,0,62,63,3,14,7,0,63,13,1,0,0,0,64,65,5,9,0,
        0,65,15,1,0,0,0,66,67,5,2,0,0,67,68,3,20,10,0,68,17,1,0,0,0,69,70,
        5,4,0,0,70,71,5,16,0,0,71,72,3,20,10,0,72,19,1,0,0,0,73,74,6,10,
        -1,0,74,81,5,9,0,0,75,81,5,4,0,0,76,77,5,5,0,0,77,78,3,20,10,0,78,
        79,5,6,0,0,79,81,1,0,0,0,80,73,1,0,0,0,80,75,1,0,0,0,80,76,1,0,0,
        0,81,96,1,0,0,0,82,83,10,5,0,0,83,84,5,12,0,0,84,95,3,20,10,6,85,
        86,10,4,0,0,86,87,5,14,0,0,87,95,3,20,10,5,88,89,10,3,0,0,89,90,
        5,15,0,0,90,95,3,20,10,4,91,92,10,2,0,0,92,93,5,13,0,0,93,95,3,20,
        10,3,94,82,1,0,0,0,94,85,1,0,0,0,94,88,1,0,0,0,94,91,1,0,0,0,95,
        98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,21,1,0,0,0,98,96,1,0,0,
        0,99,100,5,3,0,0,100,101,5,5,0,0,101,102,3,20,10,0,102,103,5,6,0,
        0,103,23,1,0,0,0,104,105,5,3,0,0,105,106,5,5,0,0,106,107,5,4,0,0,
        107,109,5,5,0,0,108,110,3,12,6,0,109,108,1,0,0,0,109,110,1,0,0,0,
        110,111,1,0,0,0,111,112,5,6,0,0,112,113,5,6,0,0,113,25,1,0,0,0,9,
        29,33,39,48,55,80,94,96,109
    ]

class grammarTraductorParser ( Parser ):

    grammarFileName = "grammarTraductor.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'return'", "'print'", "<INVALID>", 
                     "'('", "')'", "','", "':'", "<INVALID>", "'\\t'", "'\\n'", 
                     "'*'", "'/'", "'+'", "'-'", "'='" ]

    symbolicNames = [ "<INVALID>", "DEF", "RETURN", "PRINT", "ID", "LPAREN", 
                      "RPAREN", "COMMA", "TWOPOINTS", "NUMERO", "TAB", "JUMP", 
                      "MUL", "DIV", "ADD", "SUB", "EQUAL", "WS", "ERROR" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_functionDef = 2
    RULE_statements = 3
    RULE_paramList = 4
    RULE_param = 5
    RULE_paraNumberList = 6
    RULE_paramNumber = 7
    RULE_return = 8
    RULE_igualation = 9
    RULE_expression = 10
    RULE_printStatement = 11
    RULE_printResults = 12

    ruleNames =  [ "program", "statement", "functionDef", "statements", 
                   "paramList", "param", "paraNumberList", "paramNumber", 
                   "return", "igualation", "expression", "printStatement", 
                   "printResults" ]

    EOF = Token.EOF
    DEF=1
    RETURN=2
    PRINT=3
    ID=4
    LPAREN=5
    RPAREN=6
    COMMA=7
    TWOPOINTS=8
    NUMERO=9
    TAB=10
    JUMP=11
    MUL=12
    DIV=13
    ADD=14
    SUB=15
    EQUAL=16
    WS=17
    ERROR=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarTraductorParser.StatementContext)
            else:
                return self.getTypedRuleContext(grammarTraductorParser.StatementContext,i)


        def getRuleIndex(self):
            return grammarTraductorParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = grammarTraductorParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.statement()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDef(self):
            return self.getTypedRuleContext(grammarTraductorParser.FunctionDefContext,0)


        def printResults(self):
            return self.getTypedRuleContext(grammarTraductorParser.PrintResultsContext,0)


        def getRuleIndex(self):
            return grammarTraductorParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = grammarTraductorParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.functionDef()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.printResults()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEF(self):
            return self.getToken(grammarTraductorParser.DEF, 0)

        def ID(self):
            return self.getToken(grammarTraductorParser.ID, 0)

        def LPAREN(self):
            return self.getToken(grammarTraductorParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(grammarTraductorParser.RPAREN, 0)

        def TWOPOINTS(self):
            return self.getToken(grammarTraductorParser.TWOPOINTS, 0)

        def statements(self):
            return self.getTypedRuleContext(grammarTraductorParser.StatementsContext,0)


        def paramList(self):
            return self.getTypedRuleContext(grammarTraductorParser.ParamListContext,0)


        def getRuleIndex(self):
            return grammarTraductorParser.RULE_functionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDef" ):
                listener.enterFunctionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDef" ):
                listener.exitFunctionDef(self)




    def functionDef(self):

        localctx = grammarTraductorParser.FunctionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(grammarTraductorParser.DEF)
            self.state = 36
            self.match(grammarTraductorParser.ID)
            self.state = 37
            self.match(grammarTraductorParser.LPAREN)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 38
                self.paramList()


            self.state = 41
            self.match(grammarTraductorParser.RPAREN)
            self.state = 42
            self.match(grammarTraductorParser.TWOPOINTS)
            self.state = 43
            self.statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_(self):
            return self.getTypedRuleContext(grammarTraductorParser.ReturnContext,0)


        def igualation(self):
            return self.getTypedRuleContext(grammarTraductorParser.IgualationContext,0)


        def printStatement(self):
            return self.getTypedRuleContext(grammarTraductorParser.PrintStatementContext,0)


        def getRuleIndex(self):
            return grammarTraductorParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = grammarTraductorParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statements)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.return_()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.igualation()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.printStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarTraductorParser.ParamContext)
            else:
                return self.getTypedRuleContext(grammarTraductorParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.COMMA)
            else:
                return self.getToken(grammarTraductorParser.COMMA, i)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)




    def paramList(self):

        localctx = grammarTraductorParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.param()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 51
                self.match(grammarTraductorParser.COMMA)
                self.state = 52
                self.param()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(grammarTraductorParser.ID, 0)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = grammarTraductorParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(grammarTraductorParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParaNumberListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramNumber(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarTraductorParser.ParamNumberContext)
            else:
                return self.getTypedRuleContext(grammarTraductorParser.ParamNumberContext,i)


        def COMMA(self):
            return self.getToken(grammarTraductorParser.COMMA, 0)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_paraNumberList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParaNumberList" ):
                listener.enterParaNumberList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParaNumberList" ):
                listener.exitParaNumberList(self)




    def paraNumberList(self):

        localctx = grammarTraductorParser.ParaNumberListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_paraNumberList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.paramNumber()

            self.state = 61
            self.match(grammarTraductorParser.COMMA)
            self.state = 62
            self.paramNumber()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(grammarTraductorParser.NUMERO, 0)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_paramNumber

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamNumber" ):
                listener.enterParamNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamNumber" ):
                listener.exitParamNumber(self)




    def paramNumber(self):

        localctx = grammarTraductorParser.ParamNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_paramNumber)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(grammarTraductorParser.NUMERO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(grammarTraductorParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarTraductorParser.ExpressionContext,0)


        def getRuleIndex(self):
            return grammarTraductorParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)




    def return_(self):

        localctx = grammarTraductorParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(grammarTraductorParser.RETURN)
            self.state = 67
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgualationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(grammarTraductorParser.ID, 0)

        def EQUAL(self):
            return self.getToken(grammarTraductorParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarTraductorParser.ExpressionContext,0)


        def getRuleIndex(self):
            return grammarTraductorParser.RULE_igualation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgualation" ):
                listener.enterIgualation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgualation" ):
                listener.exitIgualation(self)




    def igualation(self):

        localctx = grammarTraductorParser.IgualationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_igualation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(grammarTraductorParser.ID)
            self.state = 70
            self.match(grammarTraductorParser.EQUAL)
            self.state = 71
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(grammarTraductorParser.NUMERO, 0)

        def ID(self):
            return self.getToken(grammarTraductorParser.ID, 0)

        def LPAREN(self):
            return self.getToken(grammarTraductorParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarTraductorParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(grammarTraductorParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(grammarTraductorParser.RPAREN, 0)

        def MUL(self):
            return self.getToken(grammarTraductorParser.MUL, 0)

        def ADD(self):
            return self.getToken(grammarTraductorParser.ADD, 0)

        def SUB(self):
            return self.getToken(grammarTraductorParser.SUB, 0)

        def DIV(self):
            return self.getToken(grammarTraductorParser.DIV, 0)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = grammarTraductorParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 74
                self.match(grammarTraductorParser.NUMERO)
                pass
            elif token in [4]:
                self.state = 75
                self.match(grammarTraductorParser.ID)
                pass
            elif token in [5]:
                self.state = 76
                self.match(grammarTraductorParser.LPAREN)
                self.state = 77
                self.expression(0)
                self.state = 78
                self.match(grammarTraductorParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 94
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = grammarTraductorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 82
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 83
                        self.match(grammarTraductorParser.MUL)
                        self.state = 84
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = grammarTraductorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 85
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 86
                        self.match(grammarTraductorParser.ADD)
                        self.state = 87
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = grammarTraductorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 88
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 89
                        self.match(grammarTraductorParser.SUB)
                        self.state = 90
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = grammarTraductorParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 91
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 92
                        self.match(grammarTraductorParser.DIV)
                        self.state = 93
                        self.expression(3)
                        pass

             
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrintStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(grammarTraductorParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(grammarTraductorParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(grammarTraductorParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(grammarTraductorParser.RPAREN, 0)

        def getRuleIndex(self):
            return grammarTraductorParser.RULE_printStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStatement" ):
                listener.enterPrintStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStatement" ):
                listener.exitPrintStatement(self)




    def printStatement(self):

        localctx = grammarTraductorParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_printStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(grammarTraductorParser.PRINT)
            self.state = 100
            self.match(grammarTraductorParser.LPAREN)
            self.state = 101
            self.expression(0)
            self.state = 102
            self.match(grammarTraductorParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintResultsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(grammarTraductorParser.PRINT, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.LPAREN)
            else:
                return self.getToken(grammarTraductorParser.LPAREN, i)

        def ID(self):
            return self.getToken(grammarTraductorParser.ID, 0)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(grammarTraductorParser.RPAREN)
            else:
                return self.getToken(grammarTraductorParser.RPAREN, i)

        def paraNumberList(self):
            return self.getTypedRuleContext(grammarTraductorParser.ParaNumberListContext,0)


        def getRuleIndex(self):
            return grammarTraductorParser.RULE_printResults

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintResults" ):
                listener.enterPrintResults(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintResults" ):
                listener.exitPrintResults(self)




    def printResults(self):

        localctx = grammarTraductorParser.PrintResultsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_printResults)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(grammarTraductorParser.PRINT)
            self.state = 105
            self.match(grammarTraductorParser.LPAREN)
            self.state = 106
            self.match(grammarTraductorParser.ID)
            self.state = 107
            self.match(grammarTraductorParser.LPAREN)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 108
                self.paraNumberList()


            self.state = 111
            self.match(grammarTraductorParser.RPAREN)
            self.state = 112
            self.match(grammarTraductorParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[10] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




