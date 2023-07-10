# pimp
The Python Inventory Management Project

# Database Tables
Item:
 id (auto increment, primary)
 name (varchar(100))
 description (foreign key, description table)
 finance (foreign key, finance table)
 stock (foreign key, stock table)

Description:
 id
 short description
 full description

Finance:
 id
 cost (double)
 price (double)
 markup_dollars (double)
 markup_percent (double)

Stock:
 id
 current_stock (int)
 minimum_stock (int)
 reserved_stock (int)
 ordered_stock (int)
