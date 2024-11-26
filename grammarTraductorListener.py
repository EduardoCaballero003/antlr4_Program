# Generated from grammarTraductor.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .grammarTraductorParser import grammarTraductorParser
else:
    from grammarTraductorParser import grammarTraductorParser

# This class defines a complete listener for a parse tree produced by grammarTraductorParser.
class grammarTraductorListener(ParseTreeListener):

    # Enter a parse tree produced by grammarTraductorParser#program.
    def enterProgram(self, ctx:grammarTraductorParser.ProgramContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#program.
    def exitProgram(self, ctx:grammarTraductorParser.ProgramContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#statement.
    def enterStatement(self, ctx:grammarTraductorParser.StatementContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#statement.
    def exitStatement(self, ctx:grammarTraductorParser.StatementContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#functionDef.
    def enterFunctionDef(self, ctx:grammarTraductorParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#functionDef.
    def exitFunctionDef(self, ctx:grammarTraductorParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#statements.
    def enterStatements(self, ctx:grammarTraductorParser.StatementsContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#statements.
    def exitStatements(self, ctx:grammarTraductorParser.StatementsContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#paramList.
    def enterParamList(self, ctx:grammarTraductorParser.ParamListContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#paramList.
    def exitParamList(self, ctx:grammarTraductorParser.ParamListContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#param.
    def enterParam(self, ctx:grammarTraductorParser.ParamContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#param.
    def exitParam(self, ctx:grammarTraductorParser.ParamContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#paraNumberList.
    def enterParaNumberList(self, ctx:grammarTraductorParser.ParaNumberListContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#paraNumberList.
    def exitParaNumberList(self, ctx:grammarTraductorParser.ParaNumberListContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#paramNumber.
    def enterParamNumber(self, ctx:grammarTraductorParser.ParamNumberContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#paramNumber.
    def exitParamNumber(self, ctx:grammarTraductorParser.ParamNumberContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#return.
    def enterReturn(self, ctx:grammarTraductorParser.ReturnContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#return.
    def exitReturn(self, ctx:grammarTraductorParser.ReturnContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#igualation.
    def enterIgualation(self, ctx:grammarTraductorParser.IgualationContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#igualation.
    def exitIgualation(self, ctx:grammarTraductorParser.IgualationContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#expression.
    def enterExpression(self, ctx:grammarTraductorParser.ExpressionContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#expression.
    def exitExpression(self, ctx:grammarTraductorParser.ExpressionContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#printStatement.
    def enterPrintStatement(self, ctx:grammarTraductorParser.PrintStatementContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#printStatement.
    def exitPrintStatement(self, ctx:grammarTraductorParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#printResults.
    def enterPrintResults(self, ctx:grammarTraductorParser.PrintResultsContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#printResults.
    def exitPrintResults(self, ctx:grammarTraductorParser.PrintResultsContext):
        pass



del grammarTraductorParser