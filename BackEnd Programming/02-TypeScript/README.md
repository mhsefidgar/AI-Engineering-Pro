# TypeScript for Backend Development

Focus on the TypeScript features that make server code safer and easier to maintain.

## Topics

- Primitive and structural types
- Type inference and narrowing
- Interfaces vs type aliases
- Generics
- Union/discriminated union types
- Utility types
- Async/await and Promises
- Error handling
- ES modules and imports/exports
- Runtime validation versus compile-time types

The existing `Inference_Types.md` contains useful export/type examples. Treat it as a reference while adding backend-oriented examples such as typed request models, service results, repository interfaces, and error types.

## Important distinction

TypeScript types disappear at runtime. HTTP input still needs runtime validation using a schema library or framework validation layer. A compile-time interface cannot protect an API from malformed JSON sent by a client.