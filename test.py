#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import unittest
from zookeeper import Ztree


class TestingZookeeper(unittest.TestCase):
    def test_crear_estructura(self):
        tree = Ztree()
        tree.create("/node1","Contenido",False,True,0,"/")
        tree.create("/node2","data2",True,True,100,"/")
        tree.create("/node2/node3","data2",True,True,100,"/node2")
        tree.create("/node1/node4","data2",True,True,100,"/node1")
        tree.create("/node2/node3/node5","data2",True,True,100,"/")

    def test_imprimir_arbol(self):
        tree = Ztree()
        tree.create("/node1","Contenido",False,True,0,"/")
        tree.create("/node2","data2",True,True,100,"/")
        tree.create("/node2/node3","data2",True,True,100,"/node2")
        tree.create("/node1/node4","data2",True,True,100,"/node1")
        tree.create("/node5","data2",True,True,100,"/node2/node3")
        tree.showTree()

    def test_eliminar_intermedio(self):
        tree = Ztree()
        tree.create("/node1","Contenido",False,True,0,"/")
        tree.create("/node2","data2",True,True,100,"/")
        tree.create("/node2/node3","data2",True,True,100,"/node2")
        tree.create("/node1/node4","data2",True,True,100,"/node1")
        tree.create("/node5","data2",True,True,100,"/node2/node3")
        print("==== Mostrando original ====")
        tree.showTree()
        tree.delete("/node2/node3",0)
        print("==== Mostrando eliminados ====")
        tree.showTree()

    def test_obtener_nodo_falso(self):
        tree = Ztree()
        tree.create("/node1","Contenido",False,True,0,"/")
        tree.create("/node2","data2",True,True,100,"/")
        tree.create("/node2/node3","data2",True,True,100,"/node2")
        tree.create("/node1/node4","data2",True,True,100,"/node1")
        tree.create("/node5","data2",True,True,100,"/node2/node3")
        tree.getChildren("/nodo3/nodo1")


    def test_eliminar_arbol_fallo(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create("/node1","Contenido",False,True,0,"/")
            tree.create("/node2","data2",True,True,100,"/")
            tree.create("/node2/node3","data2",True,True,100,"/node2")
            tree.create("/node1/node4","data2",True,True,100,"/node1")
            tree.create("/node5","data2",True,True,100,"/node2/node3")
            tree.delete("/")


if __name__ == '__main__':
    unittest.main()
