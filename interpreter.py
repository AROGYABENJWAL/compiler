import sys

class SixenineInterpreter:
    def __init__(self):
        self.global_env = {}
        self.functions = {}
        # Increase recursion limit for recursive functions
        sys.setrecursionlimit(10000)

    def run(self, tree):
        return self.evaluate(tree, self.global_env)

    def evaluate(self, tree, env):
        if isinstance(tree, tuple):
            operation = tree[0]
            
            if operation == 'program':
                return self.evaluate(tree[1], env)
            
            elif operation == 'number':
                return tree[1]
            
            elif operation == 'string':
                return tree[1]
            
            elif operation == 'var':
                return env.get(tree[1], 0)
            
            elif operation == 'assign':
                env[tree[1]] = self.evaluate(tree[2], env)
                return env[tree[1]]
            
            elif operation == '+':
                return self.evaluate(tree[1], env) + self.evaluate(tree[2], env)
            
            elif operation == '-':
                return self.evaluate(tree[1], env) - self.evaluate(tree[2], env)
            
            elif operation == '*':
                return self.evaluate(tree[1], env) * self.evaluate(tree[2], env)
            
            elif operation == '/':
                return self.evaluate(tree[1], env) / self.evaluate(tree[2], env)
            
            elif operation == '==':
                return self.evaluate(tree[1], env) == self.evaluate(tree[2], env)
            
            elif operation == '<':
                return self.evaluate(tree[1], env) < self.evaluate(tree[2], env)
            
            elif operation == '>':
                return self.evaluate(tree[1], env) > self.evaluate(tree[2], env)
            
            elif operation == 'if':
                condition = self.evaluate(tree[1], env)
                if condition:
                    return self.evaluate_statements(tree[2], env)
                return None
            
            elif operation == 'if_else':
                condition = self.evaluate(tree[1], env)
                if condition:
                    return self.evaluate_statements(tree[2], env)
                else:
                    return self.evaluate_statements(tree[3], env)
            
            elif operation == 'while':
                while self.evaluate(tree[1], env):
                    self.evaluate_statements(tree[2], env)
                return None
            
            elif operation == 'print':
                value = self.evaluate(tree[1], env)
                print(value)
                return value
            
            elif operation == 'func_def':
                name = tree[1]
                params = tree[2]
                body = tree[3]
                self.functions[name] = (params, body)
                return None
            
            elif operation == 'call':
                func_name = tree[1]
                if func_name not in self.functions:
                    raise NameError(f"Function {func_name} not defined")
                
                params, body = self.functions[func_name]
                args = [self.evaluate(arg, env) for arg in tree[2]]
                
                if len(params) != len(args):
                    raise ValueError(f"Expected {len(params)} arguments, got {len(args)}")
                
                # Create new environment for function
                local_env = env.copy()
                for param, arg in zip(params, args):
                    local_env[param] = arg
                
                return self.evaluate_statements(body, local_env)
            
            elif operation == 'return':
                return self.evaluate(tree[1], env)

        elif isinstance(tree, list):
            return self.evaluate_statements(tree, env)

        return None

    def evaluate_statements(self, statements, env):
        result = None
        for statement in statements:
            result = self.evaluate(statement, env)
        return result 