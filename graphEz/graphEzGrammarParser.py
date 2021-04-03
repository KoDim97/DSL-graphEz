# Generated from graphEzGrammar.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("F\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\30\n\2\r\2\16\2")
        buf.write("\31\3\3\3\3\5\3\36\n\3\3\3\3\3\3\3\3\4\3\4\5\4%\n\4\3")
        buf.write("\4\5\4(\n\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\6\7\63")
        buf.write("\n\7\r\7\16\7\64\3\b\3\b\3\b\3\b\3\b\5\b<\n\b\5\b>\n\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20")
        buf.write("\22\24\2\5\3\2\b\16\4\2\b\b\20\25\3\2\26\30\2B\2\27\3")
        buf.write("\2\2\2\4\33\3\2\2\2\6\"\3\2\2\2\b+\3\2\2\2\n.\3\2\2\2")
        buf.write("\f\62\3\2\2\2\16=\3\2\2\2\20?\3\2\2\2\22A\3\2\2\2\24C")
        buf.write("\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\30\31\3\2\2\2\31")
        buf.write("\27\3\2\2\2\31\32\3\2\2\2\32\3\3\2\2\2\33\35\7\3\2\2\34")
        buf.write("\36\5\6\4\2\35\34\3\2\2\2\35\36\3\2\2\2\36\37\3\2\2\2")
        buf.write("\37 \5\f\7\2 !\7\4\2\2!\5\3\2\2\2\"$\7\5\2\2#%\5\b\5\2")
        buf.write("$#\3\2\2\2$%\3\2\2\2%\'\3\2\2\2&(\5\n\6\2\'&\3\2\2\2\'")
        buf.write("(\3\2\2\2()\3\2\2\2)*\7\6\2\2*\7\3\2\2\2+,\7\7\2\2,-\t")
        buf.write("\2\2\2-\t\3\2\2\2./\7\17\2\2/\60\t\3\2\2\60\13\3\2\2\2")
        buf.write("\61\63\5\16\b\2\62\61\3\2\2\2\63\64\3\2\2\2\64\62\3\2")
        buf.write("\2\2\64\65\3\2\2\2\65\r\3\2\2\2\66>\5\20\t\2\678\5\20")
        buf.write("\t\289\5\24\13\29;\5\20\t\2:<\5\22\n\2;:\3\2\2\2;<\3\2")
        buf.write("\2\2<>\3\2\2\2=\66\3\2\2\2=\67\3\2\2\2>\17\3\2\2\2?@\7")
        buf.write("\31\2\2@\21\3\2\2\2AB\7\32\2\2B\23\3\2\2\2CD\t\4\2\2D")
        buf.write("\25\3\2\2\2\t\31\35$\'\64;=")
        return buf.getvalue()


class graphEzGrammarParser ( Parser ):

    grammarFileName = "graphEzGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'['", "']'", "'layout'", 
                     "'dot'", "'neato'", "'twopi'", "'circo'", "'graphs'", 
                     "'fdp'", "'sfdp'", "'extension'", "'png'", "'jpg'", 
                     "'jpeg'", "'pdf'", "'ps'", "'svg'", "'->'", "'<-'", 
                     "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TEXT", "INTEGER", 
                      "SPACE" ]

    RULE_program = 0
    RULE_graph = 1
    RULE_render = 2
    RULE_layout = 3
    RULE_extension = 4
    RULE_elements = 5
    RULE_element = 6
    RULE_vertex = 7
    RULE_weight = 8
    RULE_edge = 9

    ruleNames =  [ "program", "graph", "render", "layout", "extension", 
                   "elements", "element", "vertex", "weight", "edge" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    TEXT=23
    INTEGER=24
    SPACE=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def graph(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(graphEzGrammarParser.GraphContext)
            else:
                return self.getTypedRuleContext(graphEzGrammarParser.GraphContext,i)


        def getRuleIndex(self):
            return graphEzGrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = graphEzGrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.graph()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==graphEzGrammarParser.T__0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraphContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elements(self):
            return self.getTypedRuleContext(graphEzGrammarParser.ElementsContext,0)


        def render(self):
            return self.getTypedRuleContext(graphEzGrammarParser.RenderContext,0)


        def getRuleIndex(self):
            return graphEzGrammarParser.RULE_graph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraph" ):
                listener.enterGraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraph" ):
                listener.exitGraph(self)




    def graph(self):

        localctx = graphEzGrammarParser.GraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_graph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(graphEzGrammarParser.T__0)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==graphEzGrammarParser.T__2:
                self.state = 26
                self.render()


            self.state = 29
            self.elements()
            self.state = 30
            self.match(graphEzGrammarParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RenderContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def layout(self):
            return self.getTypedRuleContext(graphEzGrammarParser.LayoutContext,0)


        def extension(self):
            return self.getTypedRuleContext(graphEzGrammarParser.ExtensionContext,0)


        def getRuleIndex(self):
            return graphEzGrammarParser.RULE_render

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRender" ):
                listener.enterRender(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRender" ):
                listener.exitRender(self)




    def render(self):

        localctx = graphEzGrammarParser.RenderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_render)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(graphEzGrammarParser.T__2)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==graphEzGrammarParser.T__4:
                self.state = 33
                self.layout()


            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==graphEzGrammarParser.T__12:
                self.state = 36
                self.extension()


            self.state = 39
            self.match(graphEzGrammarParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LayoutContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return graphEzGrammarParser.RULE_layout

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLayout" ):
                listener.enterLayout(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLayout" ):
                listener.exitLayout(self)




    def layout(self):

        localctx = graphEzGrammarParser.LayoutContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_layout)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(graphEzGrammarParser.T__4)
            self.state = 42
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << graphEzGrammarParser.T__5) | (1 << graphEzGrammarParser.T__6) | (1 << graphEzGrammarParser.T__7) | (1 << graphEzGrammarParser.T__8) | (1 << graphEzGrammarParser.T__9) | (1 << graphEzGrammarParser.T__10) | (1 << graphEzGrammarParser.T__11))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtensionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return graphEzGrammarParser.RULE_extension

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtension" ):
                listener.enterExtension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtension" ):
                listener.exitExtension(self)




    def extension(self):

        localctx = graphEzGrammarParser.ExtensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_extension)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(graphEzGrammarParser.T__12)
            self.state = 45
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << graphEzGrammarParser.T__5) | (1 << graphEzGrammarParser.T__13) | (1 << graphEzGrammarParser.T__14) | (1 << graphEzGrammarParser.T__15) | (1 << graphEzGrammarParser.T__16) | (1 << graphEzGrammarParser.T__17) | (1 << graphEzGrammarParser.T__18))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(graphEzGrammarParser.ElementContext)
            else:
                return self.getTypedRuleContext(graphEzGrammarParser.ElementContext,i)


        def getRuleIndex(self):
            return graphEzGrammarParser.RULE_elements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElements" ):
                listener.enterElements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElements" ):
                listener.exitElements(self)




    def elements(self):

        localctx = graphEzGrammarParser.ElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 47
                self.element()
                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==graphEzGrammarParser.TEXT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vertex(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(graphEzGrammarParser.VertexContext)
            else:
                return self.getTypedRuleContext(graphEzGrammarParser.VertexContext,i)


        def edge(self):
            return self.getTypedRuleContext(graphEzGrammarParser.EdgeContext,0)


        def weight(self):
            return self.getTypedRuleContext(graphEzGrammarParser.WeightContext,0)


        def getRuleIndex(self):
            return graphEzGrammarParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = graphEzGrammarParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 52
                self.vertex()
                pass

            elif la_ == 2:
                self.state = 53
                self.vertex()
                self.state = 54
                self.edge()
                self.state = 55
                self.vertex()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==graphEzGrammarParser.INTEGER:
                    self.state = 56
                    self.weight()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VertexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(graphEzGrammarParser.TEXT, 0)

        def getRuleIndex(self):
            return graphEzGrammarParser.RULE_vertex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVertex" ):
                listener.enterVertex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVertex" ):
                listener.exitVertex(self)




    def vertex(self):

        localctx = graphEzGrammarParser.VertexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vertex)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(graphEzGrammarParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WeightContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(graphEzGrammarParser.INTEGER, 0)

        def getRuleIndex(self):
            return graphEzGrammarParser.RULE_weight

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWeight" ):
                listener.enterWeight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWeight" ):
                listener.exitWeight(self)




    def weight(self):

        localctx = graphEzGrammarParser.WeightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_weight)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(graphEzGrammarParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdgeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return graphEzGrammarParser.RULE_edge

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdge" ):
                listener.enterEdge(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdge" ):
                listener.exitEdge(self)




    def edge(self):

        localctx = graphEzGrammarParser.EdgeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_edge)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << graphEzGrammarParser.T__19) | (1 << graphEzGrammarParser.T__20) | (1 << graphEzGrammarParser.T__21))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





