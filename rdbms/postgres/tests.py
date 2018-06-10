#!/usr/bin/env python 

from unittest import TestCase, TestLoader, TestSuite, TextTestRunner

from features.test_postgres_datatype import TestPostGresDataType
#from features.test_postgres_function import TestPostGresFunction
#from tables.test_postgres_table_join import TestPostGresTableJoin
#from tables.test_postgres_table_constraint import TestPostGresTableConstraint
#from tables.test_postgres_table_delete import TestPostGresTableDelete
#from tables.test_postgres_table_select import TestPostGresTableSelect
#from tables.test_postgres_table_select_group_by import TestPostGresTableSelectGroupBy
#from tables.test_postgres_table_select_order_by import TestPostGresTableSelectOrderBy
#from tables.test_postgres_table_trigger import TestPostGresTableTrigger
#from tables.test_postgres_table_update import TestPostGresTableUpdate
#from use_case.test_postgres_relationship_model import TestPostGresRelationshipModel

def my_suite():
    suite = TestSuite()
    loader = TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestPostGresDataType))
    #suite.addTest(loader.loadTestsFromTestCase(TestPostGresFunction))
    #suite.addTest(loader.loadTestsFromTestCase(TestPostGresRelationshipModel))
    #suite.addTest(loader.loadTestsFromTestCase(TestPostGresTableConstraint))
    #suite.addTest(loader.loadTestsFromTestCase(TestPostGresTableDelete))
    #suite.addTest(loader.loadTestsFromTestCase(TestPostGresTableJoin))
    #suite.addTest(loader.loadTestsFromTestCase(TestPostGresTableSelect))
    #suite.addTest(loader.loadTestsFromTestCase(TestPostGresTableSelectGroupBy))
    #suite.addTest(loader.loadTestsFromTestCase(TestPostGresTableSelectOrderBy))
    #suite.addTest(loader.loadTestsFromTestCase(TestPostGresTableTrigger))
    #suite.addTest(loader.loadTestsFromTestCase(TestPostGresTableUpdate))
    return suite

if __name__ == '__main__':
    runner = TextTestRunner(verbosity=2)
    runner.run(my_suite())
