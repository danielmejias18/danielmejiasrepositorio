#!/usr/bin/python3
import pathlib
import tkinter.ttk as ttk
from tkinter import messagebox
import pygubu
from models.db import session
from Pygubu.Pygubu.controller.product import Product

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "productView.ui"


class ProductviewApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        self.mainwindow = builder.get_object("toplevel1", master)

        self.variableId = None
        self.variableDescription = None
        self.variablePrice = None
        self.variableQuantity = None
        builder.import_variables(
            self,
            ["variableId", "variableDescription", "variablePrice", "variableQuantity"],
        )

        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def Add(self):
        sessionX = session()
        productX = Product(
            id = self.variableId.get(),
            description = self.variableDescription.get(),
            price = self.variablePrice.get(),
            quantity = self.variableQuantity.get(),
            statusP = Product.states.ACTIVE
            )
        sessionX.add(productX)
        messagebox.showinfo("congrats", "Product added ")
        sessionX.commit()
        sessionX.close()
    
    def Search(self):
        sessionX = session()
        productFound = sessionX.get(Product, self.variableId.get())
        if productFound == None:
            messagebox.showinfo("Error", "Product not found ")
        else:
            return productFound

        sessionX.close()
    def SetSearch(self):
        product = self.Search()
        if product!= None:
            self.variableDescription.set(product.description)
            self.variablePrice.set(product.price)
            self.variableQuantity.set(product.quantity)

    """def Update(self):
        sessionX = session()
        productFound = sessionX.get(Product, self.variableId.get())
        if productFound == None:
            messagebox.showinfo("Error", "Product not found ")
            self.Clear()
        else:
            sessionX.query(Product, self.variableId.get)
            productFound.description = self.variableDescription.get()
            productFound.price = self.variablePrice.get()
            productFound.quantity = self.variableQuantity.get()
            sessionX.commit()
            sessionX.close()
            self.Clear()
            messagebox.showinfo("Error", "Product updated ")"""
    def Update(self):
        sessionX = session()
        productX = self.Search()
        if productX!=None:
            sessionX.query(Product).filter(Product.id==productX.id).update({"description": self.variableDescription.get(), "price": self.variablePrice.get(), "quantity": self.variableQuantity.get()})
            sessionX.commit()
            sessionX.close()
            messagebox.showinfo("UPDATE","The Product has been updated!")
            self.Clear()
        else:
            messagebox.showerror('Delete Error','Product not found')
            sessionX.close()
            self.Clear()

    def Delete(self):
        sessionX = session()
        productFound = sessionX.get(Product, self.variableId.get())
        if productFound == None:
            
            messagebox.showinfo("Error", "Product not found ")
        else:
            sessionX.delete(productFound)
            sessionX.commit()
            sessionX.close()
            messagebox.showinfo("Error", "Product deleted ")
            self.Clear()

    def DeleteLogical(self):
        sessionX = session()
        product = self.Search()
        if product!= None:
            sessionX.query(Product).filter(product.id==Product.id).update({"statusP":Product.states.INACTIVE})
            sessionX.commit()
            sessionX.close()
            messagebox.showerror("Error", "eliminated  ")
        else:
            messagebox.showerror("Error", "Product not found ")


    def Clear(self):
        self.variableDescription.set('')
        self.variablePrice.set('')
        self.variableQuantity.set('')
        self.variableId.set('')


if __name__ == "__main__":
    app = ProductviewApp()
    app.run()
