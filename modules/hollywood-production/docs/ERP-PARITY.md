# ERP Parity: Hollywood Production ↔ Odoo Project Management

Hollywood Production maintains functional parity with Odoo's project management module.

## Concept Mapping

| Odoo Concept | Hollywood Production | Implementation |
|--------------|----------------------|----------------|
| Project | Production | `src/models/Production.ts` |
| Task | Scene | `src/models/Scene.ts` |
| Subtask | Shot | `src/models/Shot.ts` |
| Resource | Asset (video/audio/character) | `src/models/Asset.ts` |
| Timeline | Production Schedule | `src/models/Timeline.ts` |
| Gantt Chart | Timeline View | `ui/app/productions/[id]/timeline` |
| Kanban Board | Scene Status Board | `ui/app/scenes/board` |

## Odoo Features Implemented

✅ **Project creation and management**  
✅ **Task breakdown and assignment**  
✅ **Resource allocation**  
✅ **Timeline/Gantt visualization**  
✅ **Status tracking (Kanban)**  
⏳ **Time tracking** (future)  
⏳ **Budget management** (future)

## Data Model Alignment

```typescript
// Odoo: project.project
interface Production {
  id: string;
  name: string;
  description: string;
  status: 'draft' | 'in_progress' | 'completed';
  created_at: Date;
  updated_at: Date;
  scenes: Scene[];
}

// Odoo: project.task
interface Scene {
  id: string;
  production_id: string;
  name: string;
  description: string;
  status: 'todo' | 'in_progress' | 'review' | 'done';
  assigned_to?: string;
  due_date?: Date;
  shots: Shot[];
  assets: Asset[];
}
```

## Why ERP Parity Matters

1. **Familiar workflow:** Users experienced with Odoo can immediately use Hollywood Production
2. **Migration path:** Easy to import/export between systems
3. **Enterprise readiness:** Proven project management patterns
4. **Scalability:** Can grow from individual creator to production studio

## Future Enhancements

- [ ] Time tracking integration
- [ ] Budget/cost management
- [ ] Multi-user collaboration
- [ ] Role-based permissions
- [ ] Odoo import/export adapters
