from grammarTraductorListener import grammarTraductorListener
from grammarTraductorParser import grammarTraductorParser

class TraduceCode(grammarTraductorListener):
    def __init__(self, file):
        self.file = file  # Guardamos el archivo donde escribir

    # Enter a parse tree produced by grammarTraductorParser#program.
    def enterProgram(self, ctx:grammarTraductorParser.ProgramContext):
        self.file.write("public class Main { \n")

    # Exit a parse tree produced by grammarTraductorParser#program.
    def exitProgram(self, ctx:grammarTraductorParser.ProgramContext):
        self.file.write("\n}\n\n")  # Cierre de la función

    # Enter a parse tree produced by grammarTraductorParser#statement.
    def enterStatement(self, ctx:grammarTraductorParser.StatementContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#statement.
    def exitStatement(self, ctx:grammarTraductorParser.StatementContext):
        pass

    # Método que se ejecuta cuando entra en una declaración de función
    def enterFunctionDef(self, ctx:grammarTraductorParser.FunctionDefContext):
        func_name = ctx.children[1].getText()  # Nombre de la función
        self.file.write(f"\tpublic static void {func_name}")

    def exitFunctionDef(self, ctx:grammarTraductorParser.FunctionDefContext):
        self.file.write("\n}\n\n")  # Cierre de la función

    # Enter a parse tree produced by grammarTraductorParser#statements.
    def enterStatements(self, ctx:grammarTraductorParser.StatementsContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#statements.
    def exitStatements(self, ctx:grammarTraductorParser.StatementsContext):
        pass

    # Enter a parse tree produced by grammarTraductorParser#paramList.
    def enterParamList(self, ctx:grammarTraductorParser.ParamListContext):
        expr = ctx.getText()
        self.file.write(f"({expr}){{ \n")

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


    # Enter a parse tree produced by grammarTraductorParser#returnStatement.
    def enterReturn(self, ctx:grammarTraductorParser.ReturnContext):
        self.file.write(f"Return")

    # Exit a parse tree produced by grammarTraductorParser#returnStatement.
    def exitReturn(self, ctx:grammarTraductorParser.ReturnContext):
        self.file.write(f"ExitReturn")


    # Enter a parse tree produced by grammarTraductorParser#igualation.
    def enterIgualation(self, ctx:grammarTraductorParser.IgualationContext):
        var_name = ctx.children[0].getText()  # Nombre de la función
        value = ctx.children[2].getText()
        self.file.write(f"\t\tint {var_name} = {value};\n")

    # Exit a parse tree produced by grammarTraductorParser#igualation.
    def exitIgualation(self, ctx:grammarTraductorParser.IgualationContext):
        pass

    # Método para procesar expresiones y escribirlas
    def enterExpression(self, ctx:grammarTraductorParser.ExpressionContext):
        pass

    # Exit a parse tree produced by grammarTraductorParser#expression.
    def exitExpression(self, ctx:grammarTraductorParser.ExpressionContext):
        pass


    # Método que se ejecuta cuando entra en una declaración de impresión
    def enterPrintStatement(self, ctx:grammarTraductorParser.PrintStatementContext):
        self.file.write(f"Print")

    # Exit a parse tree produced by grammarTraductorParser#printStatement.
    def exitPrintStatement(self, ctx:grammarTraductorParser.PrintStatementContext):
        pass


    # Enter a parse tree produced by grammarTraductorParser#printResults.
    def enterPrintResults(self, ctx:grammarTraductorParser.PrintResultsContext):
        print_expr = ctx.children[2].getText()  # La expresión a imprimir
        self.file.write(f"System.out.println({print_expr});\n")

    # Exit a parse tree produced by grammarTraductorParser#printResults.
    def exitPrintResults(self, ctx:grammarTraductorParser.PrintResultsContext):
        pass