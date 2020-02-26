#pragma once

namespace logic {
namespace lights {
enum class role {
  headlights,
  headlights_full,
  headlights_full_momentary,
  reverse,
  brake,
};

void init();

void set_role(role const r);
void clear_role(role const r);
void clear_all_roles();
bool role_is_enabled(role const r);

void output();
} // namespace lights
} // namespace logic
