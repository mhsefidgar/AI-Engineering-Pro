## **1️⃣ Variables / Constants / Let / Var**

**You can export any runtime value.**

**`// math.ts`**  
**`export const PI = 3.1416;`**  
**`export let counter = 0;`**  
**`export var name = "TypeScript";`**

**Usage:**

**`import { PI, counter, name } from './math';`**

**`console.log(PI);       // 3.1416`**  
**`counter += 1;`**  
**`console.log(name);     // TypeScript`**

* **Exists at runtime, can hold actual data.**

---

## **2️⃣ Functions**

**Functions are first-class citizens in TS/JS, so you can export them.**

**`// utils.ts`**  
**`export function add(a: number, b: number): number {`**  
  **`return a + b;`**  
**`}`**

**`export const multiply = (a: number, b: number) => a * b;`**

**Usage:**

**`import { add, multiply } from './utils';`**

**`console.log(add(2,3));      // 5`**  
**`console.log(multiply(2,3)); // 6`**

---

## **3️⃣ Classes**

**Classes can be exported and instantiated elsewhere.**

**`// models.ts`**  
**`export class User {`**  
  **`constructor(public name: string, public age: number) {}`**  
  **`greet() {`**  
    **``console.log(`Hello, ${this.name}`);``**  
  **`}`**  
**`}`**

**Usage:**

**`import { User } from './models';`**

**`const u = new User("Mohammad", 30);`**  
**`u.greet(); // Hello, Mohammad`**

---

## **4️⃣ Interfaces**

**Interfaces define type shapes — they don’t exist at runtime, only for type checking.**

**`// types.ts`**  
**`export interface ModelResponse {`**  
  **`output: string;`**  
  **`latencyMs: number;`**  
  **`tokensUsed?: number;`**  
  **`costUsd?: number;`**  
**`}`**

**Usage:**

**`import { ModelResponse } from './types';`**

**`const response: ModelResponse = {`**  
  **`output: "OK",`**  
  **`latencyMs: 120,`**  
**`};`**

* **You cannot create `new ModelResponse()` — interfaces disappear after compilation.**

---

## **5️⃣ Types / Type Aliases**

**Similar to interfaces, but more flexible.**

**`// types.ts`**  
**`export type ID = string | number;`**  
**`export type Callback = (success: boolean) => void;`**

**Usage:**

**`import { ID, Callback } from './types';`**

**`let userId: ID = 123;`**  
**`const cb: Callback = (success) => console.log(success);`**

---

## **6️⃣ Enums**

**Enums are runtime objects and can be exported.**

**`// enums.ts`**  
**`export enum Status {`**  
  **`Pending,`**  
  **`Success,`**  
  **`Error,`**  
**`}`**

**Usage:**

**`import { Status } from './enums';`**

**`let s = Status.Success;`**  
**`console.log(s); // 1`**

---

## **7️⃣ Namespaces / Modules (less common in modern TS)**

**`export namespace MathUtils {`**  
  **`export const square = (x: number) => x * x;`**  
**`}`**

**Usage:**

**`import { MathUtils } from './math';`**

**`console.log(MathUtils.square(5)); // 25`**

**Note: Modern TypeScript uses ES modules (`import/export`) instead of namespaces most of the time.**

---

## **8️⃣ Exporting Everything at Once / Default Exports**

* **Named export: `export const foo = 1;` → must use `{ foo }` when importing.**

* **Default export: `export default class MyClass {}` → can import with any name:**

**`// MyClass.ts`**  
**`export default class MyClass {}`**

**`// usage`**  
**`import AnyName from './MyClass';`**  
**`const obj = new AnyName();`**

* **You cannot have more than one default export per file.**

---

## **9️⃣ Re-exporting from another file**

**`// index.ts`**  
**`export { User } from './models';`**  
**`export { ModelResponse } from './types';`**

* **Lets you create a centralized module.**

---

### **✅ Summary Table**

| Exportable | Runtime? | Usage Example |
| ----- | ----- | ----- |
| **Variable / Const / Let / Var** | **✅** | **`export const PI = 3.14;`** |
| **Function** | **✅** | **`export function add() {}`** |
| **Class** | **✅** | **`export class User {}`** |
| **Interface** | **❌** | **`export interface ModelResponse {}`** |
| **Type / Type Alias** | **❌** | **\`export type ID \= string** |
| **Enum** | **✅** | **`export enum Status {}`** |
| **Namespace** | **✅** | **`export namespace Utils {}`** |
| **Default Export** | **✅** | **`export default class MyClass {}`** |
| **Re-export** | **✅** | **`export { X } from './file';`** |

